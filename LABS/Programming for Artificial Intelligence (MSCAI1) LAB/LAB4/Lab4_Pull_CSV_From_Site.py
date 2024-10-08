import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

# Initialize lists to store the extracted data
property_names = []
property_prices = []
property_links = []

# Base URL to handle pagination
base_url = "https://www.daft.ie/property-for-sale/dublin?page="

# Function to fetch URL with retries and User-Agent header
def fetch_url(url, retries=3, backoff_factor=0.3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for i in range(retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        elif response.status_code == 503:
            print(f"Service unavailable (503). Retrying in {backoff_factor * (2 ** i)} seconds...")
            time.sleep(backoff_factor * (2 ** i))
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None
    return None

# Loop through the first 5 pages
for page_num in range(1, 6):  # Scrape the first 5 pages
    paginated_url = base_url + str(page_num)

    # Send GET request
    response = fetch_url(paginated_url)
    if not response:
        print(f"Failed to retrieve data from page {page_num}.")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the property listings on the page
    property_listings = soup.find_all('li', class_='SearchPage__Result-gg133s-2')

    if not property_listings:
        print(f"No listings found on page {page_num}. Check if the class names have changed.")

    # Extract details from each listing
    for property_listing in property_listings:
        # Extract property name
        name = property_listing.find('a', class_='PropertyInformationCommonStyles__Address-sc-1xz5tcj-8')
        if name:
            property_names.append(name.get_text(strip=True))
        else:
            property_names.append('N/A')  # Handle missing name

        # Extract property price
        price = property_listing.find('span', class_='PropertyInformationCommonStyles__CostAmount-sc-1xz5tcj-2')
        if price:
            property_prices.append(price.get_text(strip=True))
        else:
            property_prices.append('N/A')  # Handle missing price

        # Extract property link
        link = property_listing.find('a', class_='PropertyInformationCommonStyles__Address-sc-1xz5tcj-8')
        if link:
            property_links.append("https://www.daft.ie" + link['href'])
        else:
            property_links.append('N/A')  # Handle missing link

    # Sleep to avoid hitting the server too quickly
    time.sleep(2)

# Create a pandas DataFrame and save to CSV
data = pd.DataFrame({
    'Property Name': property_names,
    'Price': property_prices,
    'Link': property_links
})

data.to_csv('daft_property_listings.csv', index=False)
print("Data saved to daft_property_listings.csv")

# Optionally save to JSON as well
data_list = []
for i in range(len(property_names)):
    data_list.append({
        'Property Name': property_names[i],
        'Price': property_prices[i],
        'Link': property_links[i]
    })

with open('daft_property_listings.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("Data saved to daft_property_listings.json")