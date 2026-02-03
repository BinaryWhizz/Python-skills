# Data Transformation Methods

# Investigating distribution of numeric data

# numeric_columns = [‘column1', ‘column2’, …..]

# fig, axes = plt.subplots(num_row, num_col, figsize=(width, height))   # subplots : Create places for sub-plots within a figure
                                                                        # enumerate : Derives the elements of a given list along with their index numbers

# for index, column in enumerate(numeric_columns):
#  sns.kdeplot(data[column], ax=axes[index])
#  axes[index].set_title(‘The title for the KDE plots’) 

# plt.tight_layout()             # Ensures no overlap between the subplots 
# plt.show() 



# Shapiro Wilk test of normality

# from scipy.stats import shapiro

# numeric_columns = [‘column_1’, ‘column_2’, …..]
# shapiro_results = {}

# for column in numeric_columns:
#     stat, p_value = shapiro(data[column])           # shapiro = Function to calculate the shapiro statistics
#     shapiro_results[column] = round(p_value, 3)

# shapiro_results



# Normality test
# A data has been loaded in the variable final_data.
# Two numeric columns from the given data 'Days Present' and 'Sales Revenue Generated' are stored within 
# a variable called numeric_columns.
# Write necessary python code for:
# Import the function to perform shapiro wilk test
# Create a blank dictionary and load it into shapiro_results
# Create a for loop to calculate the stat and p_value of the shapiro test for each column within numeric_columns
# Add the column names and their correspondent p_value of shapiro statistics within shapiro_results
# Keep the p_value up to 3 decimal points
# Finally, show the output within shapiro_results

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)
numeric_columns = ['Days Present', 'Sales Revenue Generated']

from scipy.stats import shapiro

shapiro_results = {}

for col in numeric_columns:
    stat, p_value = shapiro(final_data[col])
    shapiro_results[col] = round(p_value, 3)

shapiro_results




# Starting with square root transformation

import numpy as np
def sqrt_transformation(data, column_name):
    data[f'{column_name}_sqrt'] = np.sqrt(data[column_name])     # sqrt = Function to perform square root transformation
    tat, p_value = shapiro(data[f'{column_name}_sqrt'])
    distribution = sns.kdeplot(data[f'{column_name}_sqrt'])      # f'{column_name}_sqrt = It takes the actual column name and add _sqrt with the real name

    print(distribution)
    print('p-value: ', p_value)




# SQRT transformation
# A data has been loaded in the variable final_data.
# Write necessary python code for:
# Perform square root transformation on 'Days Present'
# Include the transformed values in a new column named 'Days Present SQRT'
# Perform the shapiro test for normality and find the p_value of 'Days Present SQRT'
# Finally, print the p_value

import pandas as pd
import numpy as np
from scipy.stats import shapiro

final_data = pd.read_csv("practice_data.csv", header=0)

# Square root transformation
final_data['Days Present SQRT'] = np.sqrt(final_data['Days Present'])

# Shapiro-Wilk test for normality
stat, p_value = shapiro(final_data['Days Present SQRT'])

# Print the p-value
print(round(p_value, 3))




def log_transformation(data, column_name):
    data[f'{column_name}_log'] = np.log(data[column_name])     # log = Function to perform log transformation
    stat, p_value = shapiro(data[f'{column_name}_log'])
    distribution = sns.kdeplot(data[f'{column_name}_log'])     # f'{column_name}_log' = It takes the actual column name and add _log with the real name

    print(distribution)
    print('p-value: ', p_value)




# LOG transformation
# A data has been loaded in the variable final_data.
# Write necessary python code for:
# Perform logarithmic transformation on 'Days Present'
# Include the transformed values in a new column named 'Days Present LOG'
# Perform the shapiro test for normality and find the p_value of 'Days Present LOG'
# Finally, print the p_value

import pandas as pd
import numpy as np
from scipy.stats import shapiro

final_data = pd.read_csv("practice_data.csv", header=0)

# Logarithmic transformation
final_data['Days Present LOG'] = np.log(final_data['Days Present'])

# Shapiro-Wilk test for normality
stat, p_value = shapiro(final_data['Days Present LOG'])

# Print the p-value
print(round(p_value, 3))


