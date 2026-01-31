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


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy= 'median')
imputer.fit(data[["Income"]])
data[["Income"]] = imputer.transform(data[['income']])

imputer_2 = SimpleImputer(strategy = 'most_frequent')
imputer_2.fit(data[['City']])
data[['City']] = imputer_2.transform(data[['city']])

missing_values = data.isnull().sum()
print("Missing values:")
missing_values


# imputing missing values

# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Age
# There are some missing values within the Age variable
# Import SimpleImputer. Write necessary code to impute the missing values within Age by the 
# median age value. 

import pandas as pd

data = pd.read_csv("practice_data.csv", header=0)


from sklearn.impute import SimpleImputer

# Create the imputer with median strategy
imputer = SimpleImputer(strategy='median')

# Impute missing values in the Age column
data['Age'] = imputer.fit_transform(data[['Age']])



# Exploring dataTypes in a dataframe

data.dtypes


# Checking data types

# A dataset has been created for you and loaded into the variable data
# Write necessary code to show the data types associated with each column in the data.

import pandas as pd

data = pd.read_csv("practice_data.csv", header=0)

data.dtypes


# Dealing with inconsistent values

unique_values = data['Customer_Lifespan_Months'].unique()
unique_values

data = data[data["Customer_Lifespan_Months"] != 'xxxx'] 

data["Customer_Lifespan_Months"].unique() 



# Finding the unique values

# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Height
# Write necessary code to find the unique values of the variable Height. 
# Keep the unique values in a new variable named unique_values. Finally, call the unique_values.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

unique_values = data['Height'].unique()
unique_values


# Removing inconsistent value
# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Height
# The variable has an inconsistent value of 873734544
# Write necessary code to remove the inconsistent value from the variable Height. 
# Keep the data without inconsistent value within the variable data.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

data = data[data['Height'] != 873734544]


# Assigning correct data types

data = data[data["Customer_Lifespan_Months"] != 'xxxx'] 

data["Customer_Lifespan_Months"].unique() 

data['Customer_Lifespan_Months'] = data['Customer_Lifespan_Months'].astype(int)

data['Date_of_Purchase'] = data['Date_of_Purchase'].astype('datetime64')

data.dtypes

data.head() 



# Assigning data type

# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Income
# By default the variable was assigned with float type data.
# Write necessary code to assign the integer data type for the variable Income.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

data['Income'] = data['Income'].astype(int)



# Dealing with the duplicate values 

duplicates = data.duplicated()
data[duplicates]

data.drop_duplicates(inplace = True)

#checking
duplicates = data.duplicated()
data[duplicates]



# Identify duplicates

# A dataset has been created for you and loaded into the variable data
# The dataset has a duplicated row
# Write necessary code to find the duplicated row from the data. 
# Keep the duplicated row within the variable duplicates. 
# Filter out and show the duplicated row from the data.

# import pandas as pd
# data = pd.read_csv("practice_data.csv", header=0)

# duplicates = data[data.duplicated()]
# data[duplicates]

# or

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Write your code here
duplicates = data.duplicated()
data[duplicates]



# Removing duplicates

# A dataset has been created for you and loaded into the variable data
# The dataset has a duplicated row
# Write necessary code to remove the duplicated row from the data. Keep the inplace operation TRUE.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

data.drop_duplicates(inplace=True)
