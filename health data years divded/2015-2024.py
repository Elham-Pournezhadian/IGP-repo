#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

def process_csv_file(file_path):
    # Read the CSV file with no header
    data = pd.read_csv(file_path, header=None)

    # Extract header rows
    header1 = list(data.iloc[0, :])
    header2 = list(data.iloc[1, :])

    # Process header1
    temp_value = np.nan
    for i in range(len(header1)-1):
        if not pd.isna(header1[i]):
            temp_value = header1[i]
        else:
            header1[i] = temp_value

    # Combine header1 and header2
    for i in range(len(header2)):
        if not pd.isna(header1[i]):
            header2[i] = header1[i] + ' ' + header2[i]

    # Remove header rows from data
    data = data.iloc[2:, :]

    # Set the processed headers to the DataFrame columns
    data.columns = header2

    return data

# Example usage
file_path="E:/data/helath data/health data years divded/2015-2017.csv"
data_2015_2017 = process_csv_file(file_path)

# For data_2018_2024
file_path = "E:/data/helath data/health data years divded/2018-2024.csv"
data_2018_2024 = process_csv_file(file_path)

file_path = "E:/data/helath data/health data years divded/2017-2018.csv"
data_2017_2018 = process_csv_file(file_path)

columns_to_drop = ['Percentage of attendances within 4 hours Percentage in 4 hours or less (all)',
       'Percentage of attendances within 4 hours Percentage in 4 hours or less (type 1)',
       'Percentage of attendances within 4 hours Percentage in 4 hours or less (type 2)',
       'Percentage of attendances within 4 hours Percentage in 4 hours or less (type 3)']
data_2018_2024 = data_2018_2024.drop(columns=columns_to_drop)

columns_to_drop = ['Percentage of attendances within 4 hours Percentage in 4 hours or less (type 1)',
       'Percentage of attendances within 4 hours Percentage in 4 hours or less (all)']
data_2017_2018 = data_2017_2018.drop(columns=columns_to_drop)

data_2017_2024  = pd.concat([data_2018_2024, data_2017_2018]) 

New_Column1 = data_2015_2017['A&E attendances Type 1 Departments - Major A&E'].astype(float) - data_2015_2017['A&E attendances > 4 hours from arrival to admission, transfer or discharge Type 1 Departments - Major A&E'].astype(float)
New_Column2 = data_2015_2017['A&E attendances Type 2 Departments - Single Specialty'].astype(float) - data_2015_2017['A&E attendances > 4 hours from arrival to admission, transfer or discharge Type 2 Departments - Single Specialty'].astype(float)
New_Column3 = data_2015_2017['A&E attendances Type 3 Departments - Other A&E/Minor Injury Unit'].astype(float) - data_2015_2017['A&E attendances > 4 hours from arrival to admission, transfer or discharge Type 3 Departments - Other A&E/Minor Injury Unit'].astype(float)
New_Column4 = data_2015_2017['A&E attendances Total attendances'].astype(float) - data_2015_2017['A&E attendances > 4 hours from arrival to admission, transfer or discharge Total Attendances > 4 hours'].astype(float)

data_2015_2017.insert(loc=7, column='A&E attendances less than 4 hours from arrival to admission, transfer or discharge Type 1 Departments - Major A&E', value=New_Column1)
data_2015_2017.insert(loc=8, column='A&E attendances less than 4 hours from arrival to admission, transfer or discharge Type 2 Departments - Single Specialty', value=New_Column2)
data_2015_2017.insert(loc=9, column='A&E attendances less than 4 hours from arrival to admission, transfer or discharge Type 3 Departments - Other A&E/Minor Injury Unit', value=New_Column3)
data_2015_2017.insert(loc=10, column='A&E attendances less than 4 hours from arrival to admission, transfer or discharge Total Attendances < 4 hours', value=New_Column4)


columns_to_drop = ['A&E attendances > 4 hours from arrival to admission, transfer or discharge Percentage in 4 hours or less (type 1)',
       'A&E attendances > 4 hours from arrival to admission, transfer or discharge Percentage in 4 hours or less (all)']
data_2015_2017 = data_2015_2017.drop(columns=columns_to_drop)


data_2015_2017.columns=data_2017_2024.columns
data_2015_2024  = pd.concat([data_2017_2024, data_2015_2017])

data_2015_2024.to_csv('E:/data/helath data/health data years divded/2015-2024.csv',index=False)

