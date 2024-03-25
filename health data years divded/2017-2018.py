#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np 

# Directory containing the Excel files
directory = 'E:/data/helath data/health data years divded/2017-2018'

# Get a list of all files in the directory
files = os.listdir(directory)

# Filter the list to include only Excel files
excel_files = [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]

# Read the first Excel file to initialize the DataFrame
temp_df = pd.read_excel(os.path.join(directory, excel_files[0]))

# Extract data based on condition
data = temp_df.iloc[17:, 1:-1]
date = excel_files[0].replace(".xls", "")
filtered_data = data[data['Unnamed: 3'].str.contains('Bristol', case=False, na=False)]

# Create a list of dates corresponding to the filtered data
dates = [date] * filtered_data.shape[0]
temp_df = filtered_data
temp_df['dates'] = dates

# Iterate over each subsequent Excel file
for file in excel_files[1:]:
    df = pd.read_excel(os.path.join(directory, file))
    data = df.iloc[17:, 1:-1]
    date = file.replace(".xls", "")
    filtered_data = data[data['Unnamed: 3'].str.contains('Bristol', case=False, na=False)]
    dates = [date] * filtered_data.shape[0]
    filtered_data['dates'] = dates
    temp_df = pd.concat([temp_df, filtered_data], axis=0)

# Extract header information
header = df.iloc[13:15, 1:-1]
header['dates'] = [np.nan, 'dates']

# Concatenate header and data, and write to CSV file
concatenated_data = pd.concat([header, temp_df], axis=0)
output_filename = 'E:/data/helath data/health data years divded/2017-2018.csv'
concatenated_data.to_csv(output_filename, header=False, index=False)


# In[ ]:




