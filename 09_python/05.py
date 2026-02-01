# Data Manipulation 


data = pd.read_csv("practice_data.csv")


# In[24]:


sorted_data = data.sort_values(by = 'Income', ascending = False)
sorted_data



# dataset sorting A dataset has been created for you and loaded into the variable data The dataset has a variable named 
# Age Write necessary code to sort the entire data based on the variable Age in descending format. Keep the data sorted 
# within the variable sorted_data. Finally, call the variable sorted_data.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)
# Sort the dataset by Age in descending order
sorted_data = data.sort_values(by='Age', ascending=False)
# Display the sorted data
sorted_data


# In[26]:

male_data = data[data['Gender'] == 'Male']
male_data


# Boolean filtering #1
# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Gender
# Write necessary code to filter the given data based on the column Gender excluding the  'Male' from the data. 
# Keep the filtered data within the variable female_data. Finally, call the variable female_data

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Boolean filtering excluding 'Male'
female_data = data[data['Gender'] != 'Male']
# Display the filtered data
female_data


# In[27]:

male_fre_data = male_data[male_data['Frequency_of_Purchases'] > 5]
male_fre_data


# Boolean filtering #2
# A dataset has been created for you and loaded within the variable data.
# The data has a variable named Income.
# Write necessary code to filter out the entire data where income is higher than 60000. 
# Keep the filtered data within the variable income_data. Finally, call the variable income_data .

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Filter rows where Income is greater than 60000
income_data = data[data['Income'] > 60000]
# Display the filtered data
income_data


# In[31]:

churned_male_freq = male_fre_data.query('Churn_Status == "Yes"')
churned_male_freq


# Query method
# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Height
# Write necessary code to filter the given data based on the column Height where the heights are higher than 180. 
# Keep the filtered data within the variable height_data. Finally, call the variable height_data

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Filter data using the query method where Height is greater than 180
height_data = data.query("Height > 180")
# Display the filtered data
height_data


# In[32]:

churned_male_freq_city = churned_male_freq[churned_male_freq['City'].isin(['Chicago', 'Houston'])]
churned_male_freq_city


# IsIn filtering method
# A dataset has been created for you and loaded into the variable data
# The dataset has a variable named Profession
# Write necessary code to filter the given data based on the column Profession for those who are Employed. 
# Keep the filtered data within the variable filtered_prof. Finally, call the variable filtered_prof 

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Filter data using the isin() method for Profession = 'Employed'
filtered_prof = data[data['Profession'].isin(['Employed'])]
# Display the filtered data
filtered_prof


# In[36]:

data.head()


# In[37]:

data.loc[0:4, 'CustomerID':'Region']


# Slicing with loc A dataset has been created for you and loaded into the variable data Write necessary
# code using .loc method to slice the given data to show the first 3 rows with the columns Income, Gender and Height.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Slice the first 3 rows and select specific columns using .loc
sliced_data = data.loc[:2, ['Income', 'Gender', 'Height']]
# Display the sliced data
sliced_data


# In[38]:

data.iloc[0:5, 0:6]

# Slicing with iloc
# A dataset has been created for you and loaded into the variable data
# Write necessary code using .iloc method to slice the given data to show the first 3 rows with the columns Income, 
# Gender and Height.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Slice the first 3 rows and select specific columns using .iloc
sliced_data = data.iloc[:3, [data.columns.get_loc('Income'),
                             data.columns.get_loc('Gender'),
                             data.columns.get_loc('Height')]]
# Display the sliced data
sliced_data


# In[39]:

data[(data['Customer_Lifespan_Months'] >= 2) & (data['Customer_Lifespan_Months'] <= 5)]


# Multiple conditions A dataset has been created for you and loaded into the variable data The data has a variable 
# named Weight Write necessary code to filter the entire data based on the given conditions. Weight is greater than 
# 50 Weight is lower than 100 N.B.: Both conditions must be met successfully to show the output.

import pandas as pd
data = pd.read_csv("practice_data.csv", header=0)

# Filter data where Weight is greater than 50 and less than 100
filtered_data = data[(data['Weight'] > 50) & (data['Weight'] < 100)]
# Display the filtered data
filtered_data
