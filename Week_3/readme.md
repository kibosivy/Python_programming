# Week 3: Web Scraping, Web Services & APIs 🌐

This week focused on interacting with the web using Python. We explored how to extract data from websites (web scraping), how to access data from online platforms (web services), and how to work with APIs.

---

## 📚 Topics Covered

- **Web Scraping with BeautifulSoup**
  - Sending HTTP requests using the `requests` library
  - Parsing and navigating HTML using `BeautifulSoup`
  - Extracting useful data from web pages using tag and class selectors

- **Web Services & APIs**
  - Introduction to HTTP requests and status codes
  - How web services and APIs provide structured data (e.g., JSON/XML)
  - Basics of calling APIs and parsing API responses

---

## 📁 Assignment: Jumia Product Scraper 🛒

The assignment involved scraping product information from the [Jumia Kenya "Home Makeover"](https://www.jumia.co.ke/mlp-home-makeover/) page.

### 🛠️ What the Script Does

1. **Loads the Web Page**  
   - Sends a request to the Jumia URL using `requests.get()`
   - Parses the response HTML using `BeautifulSoup`

2. **Extracts Product Data**  
   For each product on the page, the scraper collects:
   - ✅ Product Name
   - ✅ Current Price
   - ✅ Old Price (if available)
   - ✅ Discount (calculated by subtracting the current price from the old price)
   - ✅ Number of Ratings
   - ✅ Link to the product’s individual page

3. **Cleans and Processes Prices**  
   - Removes special characters (`Ksh`, commas) from price strings using `re.sub()`
   - Converts prices into integers for calculation
   - Handles cases where price data might be missing or malformed

4. **Visits Each Product Page**  
   - Opens each product’s link individually
   - Scrapes the **total number of customer reviews** from the product's page

5. **Displays the Final Output**  
   - Prints all details: product name, prices, discount, number of ratings, and total reviews

---

## 💡 Key Concepts Practiced

- HTML parsing and tag navigation
- Data cleaning using regular expressions
- Conditional logic to handle missing/invalid data
- Working with nested HTTP requests for deeper data collection
- Creating structured, readable outputs

---

## 🧠 Key Takeaway

This assignment showed how Python can be used to extract structured information from unstructured web pages. It combined several real-world skills like data scraping, cleaning, transformation, and multi-level requests — all in one script.

✅ This folder also contains the **Week 3 Assignment**: `jumia_scraper.py`
