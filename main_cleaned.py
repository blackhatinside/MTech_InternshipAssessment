# MAIN.PY

import numpy as np
import pandas as pd


table_headers = ['Employee', 'Status', 'Date of Joining (DOJ)', 'Resignation Date', 'Last Working Day', 'Salary Jan 2024', 'Feb 2024 Increment %', 'Salary Mar 2024', 'Overall Increment Since DOJ', 'Starting Salary', 'Cycle 5 Rating', 'Cycle 4 Rating', 'Cycle 3 Rating', 'Cycle 2 Rating', 'Cycle 1 Rating', 'Cycle 0 Rating', 'Cycle 5 Promotion', 'Cycle 4 Promotion', 'Cycle 3 Promotion', 'Cycle 2 Promotion', 'Cycle 1 Promotion', 'Cycle 0 Promotion', 'Grade', 'Business Group', 'Vertical', 'Direct Manager Name', 'Employee Type', 'Office City', 'Office Country', 'Gender', 'Date of Birth', 'Compa across Median', 'Address', 'Attendance (Overall)', 'Attendance (T-W-T)', 'Attendance (3 Days a Week)', 'Influencer Rank (Latest)', 'Broker Rank (Latest)', 'Manager Health Index', 'Vertical Health Index']
string_headers = ['Status', 'Cycle 5 Promotion', 'Cycle 4 Promotion', 'Cycle 3 Promotion', 'Cycle 2 Promotion', 'Cycle 1 Promotion', 'Cycle 0 Promotion', 'Grade', 'Business Group', 'Vertical', 'Employee Type', 'Office City', 'Office Country', 'Gender', 'Address']
numeric_headers = [header for header in table_headers if header not in string_headers]


# Print the Table Details
print("Total Columns: ", len(table_headers))
print("String Columns: ", len(string_headers))
print("Numeric Columns ", len(numeric_headers))

# Load the dataset
file_path = 'Master Dataset.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')


# Print before Cleaning
print("\nSample Row Before: ".upper())
print(df.iloc[16].to_dict())


# Replace empty cells with NaN
exclude_columns = ['', 'Not Found', 'Not Available']
for word in exclude_columns:
    df.replace(word, np.nan, inplace=True)


# Clean Employee and Manager columns
df['Employee'] = df['Employee'].str.replace('Employee', '').str.strip()
df['Direct Manager Name'] = df['Direct Manager Name'].str.replace('Manager', '').str.strip()


# Clean monetary values
def clean_money(value):
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', ''))
    return value
money_columns = [
    'Salary Jan 2024',
    'Salary Mar 2024',
    'Starting Salary'
]
for col in money_columns:
    df[col] = df[col].astype(str).apply(clean_money)


# Clean percentage values
def clean_percentage(value):
    if isinstance(value, str) and value not in ("Inactive", "CCI"):
        return float(value.replace('%', '')) * 100
    return value
percentage_columns = [
    'Feb 2024 Increment %',
    'Overall Increment Since DOJ',
    'Attendance (Overall)',
    'Attendance (T-W-T)',
    'Attendance (3 Days a Week)'
]
for col in percentage_columns:
    df[col] = df[col].astype(str).apply(clean_percentage)


# Clean Manager Health Index column
df['Manager Health Index'] = df['Manager Health Index'].replace('Not Available', np.nan)


# Print after Cleaning
print("\nSample Row After: ".upper())
print(df.iloc[16].to_dict())


# Summary statistics for numerical columns
def showStats(df, numeric_headers): # Convert columns to numeric, handling errors and setting invalid parsing errors as NaN
    for header in numeric_headers:
        if df[header].dtype == 'object':
            df[header] = pd.to_numeric(df[header], errors='coerce')
    print("\nSummary Statistics:".upper())
    print(df.describe(include=[np.number, 'datetime64']))
df_copy = df.copy()
numeric_headers_copy = numeric_headers.copy()
showStats(df_copy, numeric_headers_copy)


# Summary statistics for non numerical columns
for header in string_headers:
    print("\nDistribution of {}".format(header).upper())
    print(df[header].value_counts().to_string())


THIS IS THE CODE I WROTE FOR THE BELOW QUESTION

The first round would be a case study round. Please check the attachment for the dataset. The key expectations from you are as follows:

    Run detailed analytics on this dataset
    Break it down into easily digestible insights
    Undertake a predictive analysis (e.g. attrition analysis) if possible
    Also provide general insights on:
        What additional data could be used for making the analysis more detailed and useful?
        How will you collect this data?

Ok I WANT TO VISUALIZE EVERYTHING THATS PRINTED HERE AS LINE GRAPHS, BAR GRAPHS, PIE CHARTS ETC DEPENDING ON TYPE OF THE DATA.
