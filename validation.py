import tkinter as tk
from tkinter import messagebox

# Function to validate patient name input
def validate_patient_name(patient_name, available_patients):
    if patient_name not in available_patients:
        # If the patient name is invalid, suggest the closest matches
        suggestions = [name for name in available_patients if patient_name.lower() in name.lower()]
        if suggestions:
            messagebox.showerror("Invalid Input", f"Patient '{patient_name}' not found. Did you mean: {', '.join(suggestions)}?")
        else:
            messagebox.showerror("Invalid Input", f"Patient '{patient_name}' not found. Please check the spelling or select from the list.")
        return False
    return True

# Function to validate medication input
def validate_medication(medication, available_medications):
    if medication not in available_medications:
        # Suggest valid medications
        messagebox.showerror("Invalid Input", f"Medication '{medication}' is not recognized. Please select from the list: {', '.join(available_medications)}.")
        return False
    return True

# Function to validate condition input
def validate_condition(condition, available_conditions):
    if condition not in available_conditions:
        # Suggest valid conditions
        messagebox.showerror("Invalid Input", f"Condition '{condition}' is not valid. Please select from the list: {', '.join(available_conditions)}.")
        return False
    return True

# Function to check if required patient data is missing and provide feedback
def check_missing_data(patient_data):
    missing_fields = []

    # Check if key fields like Medication, Condition, etc., are missing
    if pd.isnull(patient_data['Medication'].values[0]):
        missing_fields.append("Medication")
    if pd.isnull(patient_data['Medical Condition'].values[0]):
        missing_fields.append("Medical Condition")

    if missing_fields:
        message = f"Missing data for: {', '.join(missing_fields)}.\nPlease update the patient record."
        messagebox.showerror("Missing Data", message)
        return False

    return True
