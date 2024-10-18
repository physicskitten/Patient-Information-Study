import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the healthcare dataset
health = pd.read_csv('/kaggle/input/healthcare-dataset/healthcare_dataset.csv')

# Display the first few rows of the dataset and dataset structure
print(health.head())
health.info()

# Check for duplicated rows in the dataset
duplicate_count = health.duplicated().sum()
print(f"Number of duplicated rows: {duplicate_count}")

# Display basic statistical descriptions of the dataset
print(health.describe())

# Plotting the distribution of Age
plt.figure(figsize=(12, 5))

# Histogram
plt.subplot(1, 2, 1)
health['Age'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')

# Kernel Density Estimate (KDE)
plt.subplot(1, 2, 2)
health['Age'].plot(kind='kde', color='orange')
plt.title('Age Density Plot')
plt.xlabel('Age')

plt.tight_layout()
plt.show()

# Display the count of different medical conditions
print(health['Medical Condition'].value_counts())

# Calculate and plot the gender distribution
gender_counts = health['Gender'].value_counts(dropna=False)
if gender_counts.isnull().all():
    print("No data available for gender distribution.")
else:
    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%.2f%%', colors=['blue', 'pink'])
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
print("\nBlood Type Distribution by Gender:\n", health.groupby("Gender")["Blood Type"].value_counts())

# Group by Medical Condition and Gender and display the percentage distribution
gender_condition_distribution = health.groupby("Medical Condition")["Gender"].value_counts(normalize=True) * 100
print("\nGender Distribution by Medical Condition (%):\n", gender_condition_distribution)

# Grouping by Gender, Medical Condition, and Blood Type
grouped_df = health.groupby(["Gender", "Medical Condition", "Blood Type"]).count()["Age"]
sorted_df = grouped_df.unstack().sort_values(by="Medical Condition", ascending=True)
print("\nSorted Distribution of Conditions by Gender and Blood Type:\n", sorted_df)

# Medication count analysis
medication_counts = health['Medication'].value_counts()
print("\nMedication Counts:\n", medication_counts)

# Displaying medical condition counts grouped by medication
medication_condition_counts = health.groupby('Medication')["Medical Condition"].value_counts()
print("\nMedical Condition Counts by Medication:\n", medication_condition_counts)

# Plotting the distribution of admission types
colors = plt.get_cmap('Pastel1').colors
health["Admission Type"].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    figsize=(10, 5), 
    title='Distribution of Admission Type', 
    explode=(0.11, 0, 0), 
    shadow=True, 
    colors=colors
)
plt.ylabel('')
plt.show()

# Display the count of admission types grouped by gender
admission_gender_counts = health.groupby("Gender")["Admission Type"].value_counts().unstack()
print("\nAdmission Type Counts by Gender:\n", admission_gender_counts)

# Grouping admission types by medication
admission_medication_counts = health.groupby("Admission Type")["Medication"].value_counts()
print("\nMedication Counts by Admission Type:\n", admission_medication_counts)

# Grouping data by admission type, medication, and medical condition, then counting occurrences
grouped_health = health.groupby(["Admission Type", "Medication", "Medical Condition"]).count()["Age"].unstack()
print("\nGrouped Data by Admission Type, Medication, and Medical Condition:\n", grouped_health)

# Define a dictionary to hold medication information
medication_info = {
    "Aspirin": {
        "Arthritis": "Used to manage pain and inflammation.",
        "Cancer": "May lower the risk of certain cancers (e.g., colorectal cancer) due to its anti-inflammatory effects.",
        "Diabetes": "Often prescribed to prevent cardiovascular complications.",
        "Obesity": "No direct link, but used to manage related pain or inflammation.",
        "Asthma": "Not typically recommended; can worsen asthma in sensitive individuals.",
        "Hypertension": "Used with caution as it can affect blood pressure.",
    },
    "Ibuprofen": {
        "Arthritis": "Commonly used to manage arthritis symptoms due to its anti-inflammatory properties.",
        "Cancer": "No direct evidence linking it to cancer risk, but may have some indirect benefits.",
        "Diabetes": "Generally safe but should be used cautiously in people with kidney issues.",
        "Obesity": "No direct link; used for managing related pain.",
        "Asthma": "Can sometimes worsen asthma symptoms.",
        "Hypertension": "Should be used cautiously as it can increase blood pressure.",
    },
    "Lipitor (Atorvastatin)": {
        "Arthritis": "No direct link, but may help manage cardiovascular risk associated with arthritis.",
        "Cancer": "May have a protective effect against certain cancers, but evidence is inconclusive.",
        "Diabetes": "Can increase the risk of developing diabetes in some individuals.",
        "Obesity": "Not directly linked but may be used to manage cholesterol levels.",
        "Asthma": "No direct link.",
        "Hypertension": "Used to manage cardiovascular risk factors associated with hypertension.",
    },
    "Paracetamol (Acetaminophen)": {
        "Arthritis": "Used to manage pain, but does not have anti-inflammatory properties.",
        "Cancer": "No direct link; used for pain management.",
        "Diabetes": "Generally safe but should be used cautiously in high doses.",
        "Obesity": "No direct link; used for managing pain related to obesity.",
        "Asthma": "Safe for most people with asthma.",
        "Hypertension": "Safe for most people with hypertension.",
    },
    "Penicillin": {
        "Arthritis": "No direct link; used if an infection complicates arthritis.",
        "Cancer": "No direct link; used to treat infections.",
        "Diabetes": "Safe to use, but diabetic patients need to monitor for potential side effects.",
        "Obesity": "No direct link; used for infections.",
        "Asthma": "Generally safe but can cause allergic reactions in some individuals.",
        "Hypertension": "Safe for most individuals with hypertension.",
    },
}

# Function to provide medication information based on prescription and condition
def get_medication_info(medication, condition):
    # Retrieve the medication info from the dictionary
    med_info = medication_info.get(medication, {})
    # Retrieve the condition-specific information
    condition_info = med_info.get(condition, "No specific information available for this condition.")
    
    # Display the information to the patient
    print(f"**Information for {medication}:**")
    print(f"{condition}: {condition_info}")

# Example Usage
get_medication_info("Aspirin", "Arthritis")

# Function to provide patient data and medication information
def provide_patient_info(patient_name):
    # Search for the patient by name in the DataFrame
    patient = health[health['Name'] == patient_name]
    
    # Check if the patient exists in the database
    if patient.empty:
        print(f"Patient '{patient_name}' not found. Please check the name and try again.")
        return
    
    # Extract patient details
    condition = patient['Medical Condition'].values[0]
    medication = patient['Medication'].values[0]
    
    # Retrieve medication information
    med_info = medication_info.get(medication, {})
    condition_info = med_info.get(condition, "No specific information available for this condition.")
    
    # Display patient data and medication information
    print(f"\nPatient Information for {patient_name}:")
    print(f"Age: {patient['Age'].values[0]}")
    print(f"Gender: {patient['Gender'].values[0]}")
    print(f"Condition: {condition}")
    print(f"Prescribed Medication: {medication}")
    print(f"\nMedication Advice for {medication}:")
    print(f"{condition}: {condition_info}")

# Example Usage
patient_name = input("Enter the patient's name: ")
provide_patient_info(patient_name)
