# Loading csv data
# A data has been created for you named practice_data.csv

# Import pandas as pd

# Write necessary code to load the csv data. Keep the data within the variable data.

# Use this header=0 after assigning the name  practice_data.csv within the quotation mark separating 
# by a comma. It is necessary to make sure the first row of the csv file is considered as the header of 
# the data.

# In terminal -- 
# pip install pandas

import pandas as pd

data = pd.read_csv("practice_data.csv")

data.head() 


# Identifying missing or null values 

# data : Variable that contains the dataset
# isnull : Method to find the null values for each column
# sum : Method to sum up total number of null values for each column

missing_values = data.isnull().sum()
print("Missing values:")
missing_values



# A dataset has been created for you and loaded into the variable data
# write necessary code to find the number of missing values for each column within the data.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

data.isnull().sum()