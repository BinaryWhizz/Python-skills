# Merging 

import pandas as pd

data2 = pd.read_excel('performance_data.xlsx')
data2.head()

joined_data = pd.merge(data, data2, on = 'CustomerID', how = 'inner')
joined_data.head()

joined_data.shape


# Joining 
additional_data = pd.read_excel('additional_data.xlsx')
additional_data.head()

final_data = (pd.concat([joined_data, additional_data])).reset_index(drop = True)
final_data.tail()

final_data = final_data.drop('CustomerID.1', axis = 1)
final_data.head()



# Inner joining
# Two datasets have been loaded for you:
# data_1: The practice_data.csv is loaded in the variable data_1.
# data_2: The additional_data.csv is loaded in the variable data_2.
# Write necessary code to merge data_1 with data_2 on the column EmployeeID following the inner joining method. 
# Keep the joined data in the variable joined_data. Finally, show the first 5 rows of the joined_data. 

import pandas as pd
data_1 = pd.read_csv("practice_data.csv", header=0)
data_2 = pd.read_csv("additional_data.csv", header=0)

# Perform inner join on EmployeeID
joined_data = pd.merge(data_1, data_2, on='EmployeeID', how='inner')
# Display the first 5 rows of the joined data
joined_data.head()


# Vertical concatenation
# Two datasets have been loaded for you:
# main_data: The main_data.csv is loaded in the variable main_data.
# others_data: The others_data.csv is loaded in the variable others_data.
# Write necessary code to perform the following tasks:
# concat main_data with others_data
# Perform resetting the index ensuring the value of drop is TRUE
# Keep the concatenated data within the variable final_data
# Finally, show the last 5 rows of the final_data. 

import pandas as pd
main_data = pd.read_csv("main_data.csv", header=0)
others_data = pd.read_csv("others_data.csv", header=0)

# Vertically concatenate the datasets
final_data = pd.concat([main_data, others_data], axis=0).reset_index(drop=True)
# Display the last 5 rows of the concatenated data
final_data.tail()


