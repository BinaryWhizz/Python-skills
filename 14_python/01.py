# Feature engineering methods


# Creating Total Purchase Amount Variable

# Mathematical Formula:

# Total purchase amount = Purchase frequency * average purchase amount

# Python code based on the formula:
# data['Total_Purchase_Amount'] = data['Frequency_of_Purchases'] * data['Average_Purchase_Amount']

# Creating Customer Lifetime Value Variable

# Mathematical Formula:
# Customer lifetime value = Customer’s Value * Customer’s lifespan

# Python code based on the formula:
# data['CLV'] = data['Total_Purchase_Amount'] * data['Customer_Lifespan_Months'] 



# Feature generation A data has been loaded in the variable df. We can sum up all the values of the 
# columns such as Task Completion Rates, Interpersonal Skills Rating, Decision-Making Skills Rating and Sales 
# Revenue Generated, then divide the summation by the value 4 to create a new feature average_performance_score. 
# Write necessary python code for: Create a new variable average_performance_score within the df Assign an equal 
# sign and after that a first bracket Within the bracket, filter out all the values of the given columns and after 
# deriving all the values for each assign + sign Beyond the closing bracket, assign the / sign and put the value 4 

import pandas as pd
import numpy as np

df = pd.read_csv("practice_data.csv", header=0)

df['average_performance_score'] = (
    df['Task Completion Rates'] +
    df['Interpersonal Skills Rating'] +
    df['Decision-Making Skills Rating'] +
    df['Sales Revenue Generated']
) / 4




# Extracting day, month and year

# data['year'] = data['date_variable'].dt.year
# data['month'] = data['date _variable '].dt.month
# data['day'] = data['date _variable '].dt.day



# Date element extraction

# A data has been loaded in the variable date_df. Your job is to extract day, month and year from the given 
# Date variable within the dataframe.
# Write necessary python code for:
# Extract the years and keep the output by adding a new column within the date_df and name the column Year.
# Extract the months and keep the output by adding a new column within the date_df and name the column Month.
# Extract the days and keep the output by adding a new column within the date_df and name the column Day.

import pandas as pd
import numpy as np

date_df = pd.read_csv("date_data.csv", header=0)
date_df['Date'] = date_df['Date'].astype('datetime64')

# Extract year, month, and day from Date column
date_df['Year'] = date_df['Date'].dt.year
date_df['Month'] = date_df['Date'].dt.month
date_df['Day'] = date_df['Date'].dt.day



# Encoding features - LabelEncoder

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['encoded_feature'] = encoder.fit_transform(data['feature'])   # fit_transform - Fit the encoder and transform the values into numerical values



# Categorizing numeric feature

data['binned_col'] = pd.cut(data['numeric_column'],           # cut - Method to convert the numeric values into bins  
    ins=[low_val, first_range, second_range, Last_val],
    labels=['first_label', 'second_label', 'third_label'],
    include_lowest=True)
data.head()




# Feature binning
# A data has been loaded within a variable final_data. You will categorise the numeric values within the variable 
# Task Completion Rates into two categories: Faster and Slower for a new variable working_speed.
# Write necessary python code for
# Start by creating a new column within final_data named working_speed
# After the equal sign, call the relevant alias and the python method for binning
# Derive all the values of Task Completion Rates from the final_df
# Create bins and labels such a way where:
# Values higher than 50 and lower than or equal to 75 are considered as Slower
# Values higher than 75 and lower than or equal to 100 are considered as Faster
# Keep the value of include_lowest is True

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)

final_data['working_speed'] = pd.cut(
    final_data['Task Completion Rates'],
    bins=[50, 75, 100],
    labels=['Slower', 'Faster'],
    include_lowest=True
)



# Manual feature encoding 

# mapping = {cat_val: num_val, cat_val: num_val, ….}
# data['mapped_col'] = data['cat_column'].map(mapping) 



# Feature mapping
# A data has been loaded within a variable final_data. You will assign 1 for Yes and 0 for No within the column Meeting Project Deadlines.
# Write necessary python code for
# Create a dictionary for assigning 1 for Yes and 0 for No and load it in the variable mapping
# Perform mapping on the Meeting Project Deadlines variable and keep it within the existing variable

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)

# Create mapping dictionary
mapping = {'Yes': 1, 'No': 0}

# Apply mapping on Meeting Project Deadlines column
final_data['Meeting Project Deadlines'] = final_data['Meeting Project Deadlines'].map(mapping)



# Converting features into dummy 

dummies = pd.get_dummies(data[[‘cat_col_1’, ‘cat_col_2’, ……]])  # get_dummies = Method to convert unique categories into dummy values and variables
data = pd.concat([data, dummies], axis=1)




# Generating dummies
# A data has been loaded within a variable final_data. You will create dummies for the variable 
# department in the dataframe and add the dummies with the dataframe.
# Write necessary python code for
# Create dummies for the column department and load it within the variable dummies
# Perform concatenation with dummies and final_data by column and keep the output within the variable final_data

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)

# Create dummies for the column 'department'
dummies = pd.get_dummies(final_data['department'])

# Concatenate dummies and final_data by column (axis=1)
final_data = pd.concat([final_data, dummies], axis=1)

# Display the first few rows to verify
print(final_data.head())

