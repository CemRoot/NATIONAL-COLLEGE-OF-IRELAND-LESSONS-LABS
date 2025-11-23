import numpy as np
import pandas as pd

# Step 1: Load the item properties datasets
df_part1 = pd.read_csv("archive/item_properties_part1.csv")
df_part2 = pd.read_csv("archive/item_properties_part2.csv")

# Combine both parts of item properties
df_properties = pd.concat([df_part1, df_part2])

# Optional: Free up memory by deleting individual parts
del df_part1, df_part2

# Step 2: Explore available properties to identify price, stock, and other relevant fields
unique_properties = df_properties["property"].unique()
print("Unique properties:", unique_properties)

# Step 3: Extract possible numerical properties (e.g., price)
# We're assuming numerical values start with 'n', as per Kaggle's dataset description.
df_numeric_properties = df_properties[
    df_properties["value"].str.startswith("n", na=False)
]

# Check how many unique item ids have numerical values (potentially price or other numerical properties)
print(df_numeric_properties[["itemid", "property",
      "value"]].drop_duplicates().head(10))


# Step 4: Clean the price column by removing non-numerical values
def clean_price(value):
    # Remove non-numeric characters from price strings
    try:
        # Convert the numeric part of the value
        return float(value.replace("n", ""))
    except ValueError:
        return np.nan  # If it can't be converted, return NaN


# Apply the clean_price function to the 'price' column
df_numeric_properties["cleaned_value"] = df_numeric_properties["value"].apply(
    clean_price
)

# Filter only valid numerical values (prices)
df_clean_prices = df_numeric_properties.dropna(subset=["cleaned_value"])

# Convert 'cleaned_value' column to float type
df_clean_prices["cleaned_value"] = df_clean_prices["cleaned_value"].astype(
    float)

# Step 5: Extract stock availability (assuming 'available' is the property for stock)
df_stock_properties = df_properties[df_properties["property"] == "available"]

# Check the values to see if it represents stock availability
print(df_stock_properties[["itemid", "value"]].drop_duplicates().head(10))

# Step 6: Pivot the data based on the identified properties
# We assume that property 'categoryid' represents categories, and 'available' represents stock.
# For 'price', we'll assume it's represented by a numerical value like 'nX.XXX', which we'll infer.

df_properties.sort_values(
    by=["itemid", "timestamp"], ascending=[True, False], inplace=True
)

# Pivot the data to make each product's properties columns
df_pivot = df_properties.pivot_table(
    index="itemid", columns="property", values="value", aggfunc="first"
).reset_index()

# Step 7: Rename columns based on assumed property meanings
# These column mappings may change depending on the unique properties you identify
df_pivot.rename(
    columns={
        "categoryid": "category",  # Assuming 'categoryid' represents product categories
        "888": "price",  # Replace '888' with the actual property ID for price if identified
        # Assuming 'available' represents stock status (1 = in stock, 0 = out of stock)
        "available": "stock",
    },
    inplace=True,
)

# Step 8: Handle missing data
df_pivot["price"] = (
    df_clean_prices["cleaned_value"].fillna(0).astype(float)
)  # Use cleaned prices or default to 0
df_pivot["stock"] = (
    df_pivot["stock"].fillna(1).astype(int)
)  # Default stock to 1 (available)

# Step 9: Prepare the final product dataset
df_products = df_pivot[["itemid", "price", "stock", "category"]]
df_products.rename(columns={"itemid": "product_id"}, inplace=True)

# Step 10: Save the cleaned data for MySQL insertion
df_products.to_csv("products_clean.csv", index=False)
print("Cleaned product data saved to 'products_clean.csv'.")
