import asyncio
import json
import os
from playwright.async_api import async_playwright, TimeoutError


async def scrape_menu(page, target_meals = None, target_zones = None):
    all_meals = ["breakfast", "lunch", "dinner"]
    all_zones = ["red", "yellow", "blue", "green", "purple", "pink"]

    meals_to_scrape = target_meals if target_meals  else all_meals
    zones_to_scrape = target_zones if target_zones  else all_zones

    full_menu = {}

    for meal in meals_to_scrape:
        full_menu[meal] = {}

        for zone in zones_to_scrape:
            selector = f'#tuesday h2#{meal} + div.row div.col-xs-12.col-lg-2.{zone} a.nutrition-panel'
            menu_texts = await page.locator(selector).all_inner_texts()

            if menu_texts:
                full_menu[meal][zone] = menu_texts
            else:
                full_menu[meal][zone] = ["No items"]

    return full_menu


def load_presets_from_txt(filename = "presets.txt"):
    target_meals = None
    target_zones = None

    if(os.path.exists(filename)):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("meals=") and len(line) > 6:
                    target_meals = line.split('=')[1].split(',')
                elif line.startswith("zones=") and len(line) > 6:
                    target_zones = line.split('=')[1].split(',')

    return target_meals, target_zones


async def main():
    user_input = input("Normal (N) Preset (P): ").strip().upper()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        url = "https://housing.ucdavis.edu/dining/dining-commons/tercero/"
        await page.goto(url)
        await page.locator('button.dc-menu-button').click()

        menu_data = {}

        if user_input == "N":
            menu_data = await scrape_menu(page)
        elif user_input == "P":
            custom_meals, custom_zones = load_presets_from_txt("presets.txt")
            menu_data = await scrape_menu(page, target_meals=custom_meals, target_zones=custom_zones)
        else:
            print("Invalid input, Normal scrape.")
            menu_data = await scrape_menu(page)

        print(json.dumps(menu_data, indent=4))

        await browser.close()


if __name__ == '__main__':
    menu_texts = asyncio.run(main())


