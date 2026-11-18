# UC Davis Tercero Menu Scraper

An automated, asynchronous web scraper built with Python and Playwright that fetches the daily menu from the UC Davis Tercero Dining Commons. This tool navigates the dynamic university dining website to extract individual food items, automatically organizing them into a hierarchical data structure sorted by meal times—such as Breakfast, Lunch, and Dinner—and specific dietary zones, including Red, Yellow, Blue, Green, Purple, and Pink. The final output is generated as a clean, formatted JSON string, making the data highly adaptable for parsing and integration into other applications, notification systems, or bots.

Built utilizing Python's `asyncio` library and Playwright's asynchronous API, the script ensures fast, non-blocking browser automation. A core feature of the scraper is its custom preset functionality, which allows for dynamic data filtering. Users can configure a separate text file to define specific target meals and zones. When executing the script from the terminal, the user is prompted to choose between a normal full-day scrape or a preset scrape, enabling the program to instantly filter the extracted JSON data based on those predefined parameters. 

Looking ahead, the project's development roadmap includes several major feature expansions. Planned updates include Discord webhook integration to automate daily morning menu highlights, nutritional data extraction to pull calorie and macro information from individual dish links, and dietary filtering to sort the output by vegan, vegetarian, and gluten-free offerings. Furthermore, future versions will aim to wrap the scraper in a lightweight FastAPI application to serve the daily menu data via local HTTP requests, alongside integrating a SQLite database to log historical menus and track meal frequency over the academic quarter. 

## Future Features
* **Discord Webhook Integration:** Automate a daily morning message to a Discord server with the day's highlighted meals.
* **Nutritional Data Extraction:** Expand the scraper to click through the `nutrition-panel` links and extract calorie and macro information for each dish.
* **Dietary Filtering:** Add parsing for Vegan, Vegetarian, and Gluten-Free icon flags to allow users to filter the JSON output by dietary restriction.


## Quick Start  


### Installation & Configuration
1. Clone the repository:
```bash
git clone https://github.com/yourusername/UC-Davis-Tercero-DC-Menu-Scraper.git
cd UC-Davis-Tercero-DC-Menu-Scraper

```

2. Create a virtual environment and install Playwright:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install playwright
playwright install chromium

```


3. To use the custom preset filter, create a `presets.txt` file in the root directory:
```text
meals=breakfast,dinner
zones=yellow,green

```

*(If this file is omitted or left blank, the script defaults to scraping all meals and all zones).*

### Usage

Run the script directly from your terminal:

```bash
python scraper.py

```

When prompted, type `N` for a Normal full scrape, or `P` to load the filters from your `presets.txt` file.

*(Disclaimer: This is a personal portfolio project. It is not affiliated with, maintained, or endorsed by UC Davis or UC Davis Student Housing and Dining Services.)
