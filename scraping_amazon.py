import requests
from bs4 import BeautifulSoup

API_KEY = "Your_ScrapperAPI_Key"  # Replace with your ScraperAPI key

def get_amazon_product(category):
    # Constructs the URL for the selected category
    amazon_url = f"https://www.amazon.com.br/gp/bestsellers/{category}/"
    scraper_url = f"http://api.scraperapi.com?api_key={API_KEY}&url={amazon_url}"
    
    # Defines the headers to simulate a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0"
    }

    # Makes the request using ScraperAPI
    response = requests.get(scraper_url, headers=headers)

    # Checks if the request was successful
    if response.status_code != 200:
        print(f"Error accessing the page. Code: {response.status_code}")
        return []

    # Parses the HTML response
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("div", class_="zg-grid-general-faceout")

    bestsellers = []
    
    # Extracts product information from the page
    for book in books:
        img_tag = book.find("img")
        publisher_tag = book.find("a", class_="a-size-small a-link-child")
        
        author = ""
        if publisher_tag:
            publisher_div = publisher_tag.find_next("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y")
            author = publisher_div.get_text(strip=True) if publisher_div else "Author unavailable"
        
        price_tag = book.find("span", class_="a-size-base a-color-price")
        price = ""
        if price_tag:
            price_span = price_tag.find_next("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")
            price = price_span.get_text(strip=True) if price_span else "Price unavailable"
        
        img_alt = img_tag["alt"] if img_tag and "alt" in img_tag.attrs else "Image without description"
        
        bestsellers.append({"Title": img_alt, "Price": price, "Author": author})
    
    # Displays the top 10 best sellers
    print("\n=== Best Sellers ===")
    for book in bestsellers[:10]:  # Shows the first 10
        print(f"Title: {book['Title']} | Price: {book['Price']}  | Author: {book['Author']}")

def menu():
    # List of menu options for user selection
    options = [
        "Food & Beverages", "Apps & Games", "Audiobooks", "Automotive", "Babies", 
        "Beauty", "Luxury Beauty", "Toys & Games", "Home", "CDs & Vinyl", 
        "Computers & IT", "Kitchen", "Amazon Devices & Accessories", "DVD & Blu-ray", 
        "Home Appliances", "Electronics", "Sports", "Tools & Home Improvement", 
        "Games & Consoles", "Gift Cards", "Musical Instruments", "Garden & Pool", 
        "Books", "Kindle Store", "Fashion", "Furniture", "Stationery & Office Supplies", 
        "Pet Shop", "Health & Wellness"
    ]

    # Dictionary mapping user choices to category URLs
    categories = {
        1: "grocery", 2: "mobile-apps", 3: "audible", 4: "automotive", 5: "baby-products",
        6: "beauty", 7: "premium-beauty", 8: "toys", 9: "home", 10: "music",
        11: "computers", 12: "kitchen", 13: "amazon-devices", 14: "dvd", 15: "appliances",
        16: "electronics", 17: "sports", 18: "hi", 19: "videogames", 20: "gift-cards",
        21: "musical-instruments", 22: "lawn-and-garden", 23: "books", 24: "digital-text",
        25: "fashion", 26: "furniture", 27: "office", 28: "pet-products", 29: "hpc"
    }

    while True:
        # Displays the menu for the user
        print("\n=== MAIN MENU ===")
        for index, option in enumerate(options, start=1):
            print(f"{index} - {option}")
        print(f"{len(options) + 1} - Exit")

        try:
            # User selects an option
            choice = int(input("Choose an option (1-29): "))
            
            match choice:
                case n if n in categories:
                    # Calls the function to fetch best sellers from the selected category
                    get_amazon_product(categories[n])
                case _ if choice == len(categories) + 1:
                    # Exits the program
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option! Try again.")
        except ValueError:
            print("Invalid input! Enter a number.")

menu()
