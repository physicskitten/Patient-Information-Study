# Healthcare Data Analysis and Visualisation

This project involves analysing and visualising healthcare data from a dummy dataset which includes information such as age, gender, medical condition, blood type, and prescribed medications for patients. The goal is to gain insights from the data through statistical analysis, visualisations, and patient-specific medication advice.

## Features

### 1. **Data Analysis:**
   - Load the healthcare dataset and display the first few rows.
   - Check for duplicate entries.
   - Display basic statistical summaries for numerical fields.
   - Group and count data by gender, medical conditions, blood type, and admission types.

### 2. **Visualisations:**
   - **Age Distribution**: Both histogram and kernel density estimation (KDE) plots are used to show the age distribution of patients.
   - **Medical Condition Distribution**: The distribution of various medical conditions is analysed.
   - **Gender Distribution**: A pie chart shows the gender distribution within the dataset.
   - **Test Results**: A pie chart showing the distribution of test results.
   - **Blood Type Distribution**: Blood types are grouped by gender.
   - **Admission Types**: A pie chart showing the different types of hospital admissions.

### 3. **Medication Information:**
   - A detailed dictionary is provided that contains information about medications like Aspirin, Ibuprofen, Lipitor, and Paracetamol, and their effects on various conditions (e.g., Arthritis, Cancer, Diabetes).
   - Users can get specific medication advice based on a patient's medical condition.

### 4. **Patient Information Lookup:**
   - Users can input a patient’s name and retrieve relevant details such as their age, gender, medical condition, and prescribed medication.
   - Based on the retrieved information, medication advice specific to the patient's condition is displayed.

## Future Improvements

- **Data Cleaning**: Handling missing data more robustly.
- **Interactive Interface**: Create a simple user interface (UI) for easier interaction.
- **Prediction**: Add predictive modeling for patient outcomes based on existing data.
