# Amazon Best Sellers Scraper

## Overview
This project is a Python-based web scraper that retrieves the best-selling products from different categories on Amazon. The program allows the user to select a category from a menu, fetches the top 10 best sellers from that category, and displays the product details such as title, price, and author (if applicable).

## Features
- Interactive menu for category selection
- Uses ScraperAPI to bypass Amazon's restrictions
- Extracts product details including:
  - Title
  - Price
  - Author (if applicable)
- Displays the top 10 best sellers for the selected category
- Error handling for invalid inputs and failed requests
- Exits gracefully after displaying results

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

You can install the required dependencies using:
```sh
pip install requests beautifulsoup4
```

## API Key Setup
This project uses [ScraperAPI](https://www.scraperapi.com/) to handle Amazon requests. Replace the placeholder API key in the script with your own ScraperAPI key:
```python
API_KEY = "your_scraperapi_key_here"
```

## How to Use
1. Run the script:
   ```sh
   python amazon_scraper.py
   ```
2. The main menu will display category options.
3. Enter the number corresponding to the desired category.
4. The program will fetch and display the top 10 best sellers from the selected category.
5. The script will automatically exit after displaying results.

## Example Output
```
=== MAIN MENU ===
1 - Food & Beverages
2 - Apps & Games
...
29 - Health & Wellness
30 - Exit

Choose an option (1-29): 23

=== Best Sellers ===
Title: The Book Thief | Price: R$ 39.90 | Author: Markus Zusak
Title: Harry Potter and the Sorcerer's Stone | Price: R$ 59.90 | Author: J.K. Rowling
...
Exiting...
```

## Error Handling
- If an invalid number is entered, the script prompts the user to try again.
- If an API request fails, an error message is displayed.
- If no products are found, the script informs the user.


## License
This project is for educational purposes only. Scraping Amazon data should comply with its terms of service.
