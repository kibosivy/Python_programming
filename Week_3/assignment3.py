import requests
from bs4 import BeautifulSoup

# get the page
url = "https://www.jumia.co.ke/mlp-home-makeover/"

response = requests.get(url)

# if response.status_code == 200:
#   print("Request was successful")
# else:
#   print("Request unsuccessful", response.status_code)

response.status_code

response.text

soup = BeautifulSoup(response.text,"html.parser")

# print(soup)

# products = soup.find_all("div", class_="itm col")
# print(products)


# for product in products:
#   print(product.text)

products = soup.find_all("article", class_="prd _fb col c-prd")
# print(products)

# for product in products:
#   print(product.text)


# clean price strings
import re 

for product in products:
    name_tag = product.find("h3", class_="name")
    price_tag = product.find("div", class_="prc")
    old_price_tag = product.find("div", class_="old")
    reviews_tag = product.find("div", class_="rev")
    link_tag = product.find("a", href=True)

    # clean text values

    name = name_tag.text.strip() if name_tag else "N/A"
    price_text = price_tag.text.strip() if price_tag else None
    old_price_text = old_price_tag.text.strip() if old_price_tag else None
    reviews_text = reviews_tag.text.strip() if reviews_tag else "0"
    product_url = "https://www.jumia.co.ke" + link_tag["href"] if link_tag else None

    # Discount calculation
    discount_value = "N/A"
    if price_text and old_price_text:
        price_clean = re.sub(r"[^\d]", "", price_text)
        old_price_clean = re.sub(r"[^\d]", "", old_price_text)
        try:
            price = int(price_clean)
            old_price = int(old_price_clean)
            discount_value = f"Ksh {old_price - price}"
        except ValueError:
            discount_value = "Invalid price format"

    # Visit individual product page to get full review count
    detailed_reviews = "N/A"
    if product_url:
        product_response = requests.get(product_url)
        product_soup = BeautifulSoup(product_response.text, "html.parser")
        reviews_header = product_soup.find("h2", class_="-fs14 -m -upp -ptm")
        detailed_reviews = reviews_header.text.strip() if reviews_header else "Not found"

    # print results
    print(f"Name: {name}")
    print(f"Price: {price_text if price_text else 'N/A'}")
    print(f"Old Price: {old_price_text if old_price_text else 'N/A'}")
    print(f"Discount: {discount_value}")
    print(f"Total Ratings: {reviews_text}")
    print(f"Total Reviews: {detailed_reviews}")
    print("---------")

