import csv
import requests
from bs4 import BeautifulSoup

# 1. Configuration Constants
URL = "http://books.toscrape.com/catalogue/page-1.html"
EXCHANGE_RATE_GBP_TO_INR = 108.0  # 1 GBP = 108 INR
MAX_NAME_LENGTH = 25  # Truncates long book titles for a simpler look

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def extract_product_data(url):
    print(f"Connecting to website: {url}...")
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error: Unable to fetch page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    products_list = []

    # FIXED: Added the underscore to class_
    products = soup.find_all("article", class_="product_pod")

    for product in products:
        # Extract and simplify the Book Title
        full_name = product.find("h3").find("a")["title"]
        if len(full_name) > MAX_NAME_LENGTH:
            simple_name = full_name[:MAX_NAME_LENGTH].strip() + "..."
        else:
            simple_name = full_name

        # Extract Price and convert it to Rupees
        raw_price = product.find("p", class_="price_color").text.strip()
        try:
            # Removes the '£' symbol and converts the remaining string to a number
            clean_price_str = "".join(
                c for c in raw_price if c.isdigit() or c == "."
            )
            price_in_inr = round(float(clean_price_str) * EXCHANGE_RATE_GBP_TO_INR, 2)
            price_formatted = f"₹{price_in_inr}"
        except ValueError:
            price_formatted = "Price Error"

        # FIXED: Added the underscore to class_
        rating_classes = product.find("p", class_="star-rating")["class"]
        rating = rating_classes[1] if len(rating_classes) > 1 else "No rating"

        # Add the clean data to our list
        products_list.append(
            {
                "Product Name": simple_name,
                "Price (INR)": price_formatted,
                "Rating": rating,
            }
        )

    return products_list


def save_to_csv(data, filename):
    if not data:
        print("No data found to save.")
        return

    headers = data[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Writes 'Product Name', 'Price (INR)', 'Rating'
        writer.writerows(data)  # Writes the actual rows of books

    print(f"\nSuccess! Data saved to '{filename}'")


# --- Run the Script ---
if __name__ == "__main__":
    # Step 1: Scrape and process data
    scraped_books = extract_product_data(URL)

    # Step 2: Save to a spreadsheet file
    save_to_csv(scraped_books, "final_books_in_rupees.csv")