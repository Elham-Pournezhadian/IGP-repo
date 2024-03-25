#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os  # Import the os module for file and directory operations
import pandas as pd  # Import the pandas library for data manipulation
import numpy as np  # Import the numpy library for numerical operations

# Directory containing the Excel files
directory = 'E:/data/helath data/health data years divded/2015-2017'

# Get a list of all files in the directory
files = os.listdir(directory)

# Filter the list to include only Excel files
excel_files = [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]

# Read the first Excel file to initialize the DataFrame
temp_df = pd.read_excel(os.path.join(directory, excel_files[0]))

# Extract data based on condition
data = temp_df.iloc[17:, 1:]  # Exclude first 17 rows and first column
date = temp_df.iloc[4, 2]  # Extract date from specific cell
filtered_data = data[data['Unnamed: 3'].str.contains('Bristol', case=False, na=False)]  # Filter data based on condition
dates = [date] * filtered_data.shape[0]  # Create a list of dates corresponding to the filtered data
temp_df = filtered_data
temp_df['dates'] = dates

# Iterate over each Excel file
for file in excel_files[1:]:
    df = pd.read_excel(os.path.join(directory, file))
    data = df.iloc[17:, 1:]
    date = df.iloc[4, 2]
    filtered_data = data[data['Unnamed: 3'].str.contains('Bristol', case=False, na=False)]
    dates = [date] * filtered_data.shape[0]
    filtered_data['dates'] = dates
    temp_df = pd.concat([temp_df, filtered_data], axis=0)
    
# Extract header information
header = df.iloc[13:15, 1:]
header['dates'] = [np.nan, 'dates']

# Concatenate header and data, and write to CSV file
concatenated_data = pd.concat([header, temp_df.iloc[:, :-1]], axis=0)  # Exclude the last column
concatenated_data.to_csv("E:/data/helath data/health data years divded/2015-2017.csv", header=False, index=False)


# In[ ]:




