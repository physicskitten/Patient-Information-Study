import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the healthcare dataset
health = pd.read_csv('/kaggle/input/healthcare-dataset/healthcare_dataset.csv')

# Display the first few rows of the dataset
print(health.head())

# Display the structure of the dataset
health.info()

# Check for duplicated rows in the dataset
print(f"Number of duplicated rows: {health.duplicated().sum()}")

# Display basic statistical descriptions of the dataset
print(health.describe())

# Plotting the distribution of Age
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
health['Age'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')

plt.subplot(1, 2, 2)
health['Age'].plot(kind='kde', color='orange')
plt.title('Age Density Plot')
plt.xlabel('Age')

plt.tight_layout()
plt.show()

# Display the count of different medical conditions
print(health['Medical Condition'].value_counts())

# Calculate and plot the gender distribution
male_count = health[health['Gender'] == 'Male'].shape[0]
female_count = health[health['Gender'] == 'Female'].shape[0]

# Handle missing or incorrect data entries
if pd.isna(male_count):
    male_count = 0
if pd.isna(female_count):
    female_count = 0

# Plotting the gender distribution pie chart if data is available
if male_count == 0 and female_count == 0:
    print("No data available for plotting.")
else:
    plt.figure(figsize=(6, 6))
    plt.pie([male_count, female_count], labels=['Male', 'Female'], autopct='%.2f%%', colors=['blue', 'pink'])
    plt.title('Gender Distribution')
    plt.show()
