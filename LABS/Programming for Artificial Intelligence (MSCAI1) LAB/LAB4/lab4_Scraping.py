# Code have a bug in the code, it is not working properly

import requests  # To send HTTP requests using Python
from bs4 import BeautifulSoup  # To parse HTML content

# Step 1: Send a GET request to the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully accessed the webpage.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Step 2: Parse the content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all quotes on the page
quotes = soup.find_all("div", class_="quote")

# Step 4: Extract and print the quote text and author
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print("-" * 50)  # Separator for readability
