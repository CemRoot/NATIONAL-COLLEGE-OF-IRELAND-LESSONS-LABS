"""Lab2
In this module, the Continuous Assessment (CA) includes report writing on AI topics, which may require you to perform experiments. These experiments usually require datasets. In this lab, your task is to explore various resources to find datasets suitable for your chosen topic.
Following are some of the resources where you can find datasets:
•
Research Trends – https://paperswithcode.com/datasets
Kaggle (https://www.kaggle.com/)
UCI Machine Learning Repository (https://archive.ics.uci.edu/datasets)
Google Dataset Search (https://datasetsearch.research.google.com/
The Home of the U.S. Government's Open Data (https://data.gov/)
Zenodo is a general-purpose open repository developed under the European OpenAIRE program and operated by CERN (https://zenodo.org/search?page=1&size=20&q=dataset)
Tasks:
        1- At least select one or two datasets
        2- Discuss the importance of selected datasets.
        3- List Dataset properties
        a.Size,
        b.Dimension,
        c.Granularity,
        d.Data Types of each feature
        e.Class label (Binary or Multi-Class)"""

import pandas as pd  # Import pandas library for data manipulation

# Load the dataset from the CSV file into a pandas DataFrame
dataset = pd.read_csv("payment_fraud.csv")

# Display the first 5 rows of the dataset to get an initial glimpse of the data
print("First 5 rows of the dataset:")
print(dataset.head())

# Dataset Properties

# a. Size of the dataset (number of rows and columns)
num_rows, num_columns = dataset.shape
print(f"\nSize of the dataset: {num_rows} rows, {num_columns} columns")

# b. Number of dimensions in the dataset
num_dimensions = dataset.ndim
print(f"Number of dimensions in the dataset: {num_dimensions}")

# c. Granularity of the dataset
print("\nGranularity of the dataset:")
print("Each row represents an individual payment transaction with detailed attributes.")

# d. Data types of each feature (column)
print("\nData types of each feature in the dataset:")
print(dataset.dtypes)

# e. Class Label (Binary or Multi-Class)

# List all column names in the dataset
print("\nColumns in the dataset:")
print(dataset.columns.tolist())

# Identify the class label column (change 'label' if your class column has a different name)
class_label_column = (
    "label"  # Update this if your class label column has a different name
)

# Check if the class label column exists in the dataset
if class_label_column in dataset.columns:
    # Get the unique values of the class label column
    unique_class_labels = dataset[class_label_column].unique()
    print(f"\nUnique class labels in the dataset: {unique_class_labels}")

    # Determine if the class label is binary or multi-class
    num_unique_labels = len(unique_class_labels)
    if num_unique_labels == 2:
        print("The class label is binary.")
    else:
        print(
            f"The class label is multi-class with {num_unique_labels} classes.")
else:
    print(
        f"\nClass label column '{class_label_column}' not found in the dataset.")

# Discuss the importance of the selected dataset
print("\nImportance of the selected dataset:")
print(
    "The payment fraud dataset is important for fraud detection in financial transactions."
)
print(
    "It can help in developing machine learning models to identify fraudulent activities and prevent financial losses."
)
