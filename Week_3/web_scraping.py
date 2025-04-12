import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
  print("Request was successful")
else:
  print("Request unsuccessful", response.status_code)

response.status_code

response.text

# Parse the response
soup = BeautifulSoup(response.text,"html.parser")

soup

soup.find("span",class_="text").text
quotes = soup.find_all("span",class_="text")
for quote in quotes:
  print(quote.text)

authors = soup.find_all("small",class_="author")

for author in authors:
  print(author.text)

soup.find_all("a", href = True)

links = soup.find_all("a", href = True)

for link in links:
  print(link["href"])

