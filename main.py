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

# Additional analysis of Age distribution
plt.figure(figsize=(5, 3))
health['Age'].hist(edgecolor="white", grid=False, color="#FF7F3E")
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of test results
colors = plt.get_cmap('Pastel1_r').colors
health["Test Results"].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    figsize=(7, 5), 
    title='Distribution of Test Results', 
    explode=(0.11, 0, 0), 
    shadow=True, 
    colors=colors
)
plt.show()

# Display the count of different blood types
print("Blood Type Counts:\n", health["Blood Type"].value_counts())

# Group by Gender and Blood Type and count the occurrences
print("\nBlood Type Distribution by Gender:\n", health.groupby(["Gender"])["Blood Type"].value_counts())

# Group by Medical Condition and Gender and display the percentage distribution
gender_condition_distribution = health.groupby(["Medical Condition"])["Gender"].value_counts(normalize=True) * 100
print("\nGender Distribution by Medical Condition (%):\n", gender_condition_distribution)

# Grouping by Gender, Medical Condition, and Blood Type
grouped_df = health.groupby(["Gender", "Medical Condition", "Blood Type"]).count()["Age"]
sorted_df = grouped_df.unstack().sort_values(by=["Medical Condition"], ascending=True)
print("\nSorted Distribution of Conditions by Gender and Blood Type:\n", sorted_df)

# Medication count analysis
medication_counts = health['Medication'].value_counts()
print("\nMedication Counts:\n", medication_counts)
