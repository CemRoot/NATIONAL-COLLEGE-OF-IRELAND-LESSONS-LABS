# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

"""
Step 1: Loading the dataset
We are using pandas to load the dataset into a dataframe.
If you have the dataset locally, you can replace the URL with the local file path.
"""

# url = 'https://www.kaggle.com/datasets/joebeachcapital/students-performance/download'  # Kaggle dataset URL
df = pd.read_csv(
    "StudentsPerformance_with_headers.csv"
)  # Loading the CSV file into a pandas dataframe

# Display the first few rows of the dataset
print("First 5 Rows of the Dataset:")
print(df.head())
"""
Step 2: Identifying attribute types in the dataset
Here, we will identify the types of features in the dataset: numerical and categorical.
"""

# Print the data types of each column
print("\nData Types of Each Column:")
print(df.dtypes)

# Separating categorical and numerical columns
categorical_cols = df.select_dtypes(
    include=["object"]
).columns  # Categorical attributes
numerical_cols = df.select_dtypes(include=["number"]).columns  # Numerical attributes

print("\nCategorical Columns:")
print(categorical_cols)

print("\nNumerical Columns:")
print(numerical_cols)
"""
Step 3: Descriptive statistics analysis
We will analyze the basic descriptive statistics for numerical columns.
"""

# Descriptive statistics for numerical columns
print("\nDescriptive Statistics for Numerical Columns:")
print(df[numerical_cols].describe())

# Analyze mean, median, standard deviation for each numerical column
for col in numerical_cols:
    print(f"\nAnalysis of {col} Column:")
    print(f"Mean: {df[col].mean()}")
    print(f"Median: {df[col].median()}")
    print(f"Standard Deviation: {df[col].std()}")
    print(f"Minimum: {df[col].min()}")
    print(f"Maximum: {df[col].max()}")
"""
Step 4: Frequency distribution for categorical data
We will calculate how many times each category appears in the dataset.
"""

# Frequency distribution for categorical columns
for col in categorical_cols:
    print(f"\nFrequency Distribution of {col} Column:")
    print(df[col].value_counts())
"""
Step 5: Creating a distribution plot for numerical data
We will create histograms to visualize the distribution of numerical columns.
"""

# Histograms for numerical columns
df[numerical_cols].hist(figsize=(10, 8))
plt.suptitle("Distribution of Numerical Data", fontsize=16)
plt.show()
"""
Step 6: Creating bar plots for categorical data
We will visualize the frequency of each category using bar plots.
"""

# Bar plots for categorical columns
for col in categorical_cols:
    df[col].value_counts().plot(kind="bar", figsize=(6, 4))
    plt.title(f"Distribution of {col} Column")
    plt.ylabel("Frequency")
    plt.show()
"""
At the end of this script, we will have a comprehensive analysis of both the numerical and categorical attributes in the dataset.
This covers the basic requirements of the tasks mentioned, including attribute type identification and descriptive characteristics analysis.
"""
