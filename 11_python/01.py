# Advanced Data Visualizations


# Correlation analysis via scatterplot 

# plt.figure(figsize=(value_width, value_height))
# plt.scatter(data['num_col_1'], data['num_col_2’])        # Try this first
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()




# Now, Use this one - sns.regplot(x='num_col_1', y='num_col_2', data=data) 

# plt.figure(figsize=(value_width, value_height))
# sns.regplot(x='num_col_1', y='num_col_2', data=data)     # Then try this 
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()



# Scatter plot
# The final data for analysis has been loaded for you within the variable final_data. 
# The data contains two numeric variables: Interpersonal Skills Rating and Decision-Making Skills Rating
# Write necessary code for the following tasks:
# Create a scatter plot using the mentioned two variables
# Consider Interpersonal Skills Rating as the 1st variable and Decision-Making Skills Rating as the second one

import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)

plt.figure(figsize=(8, 6))

plt.scatter(
    final_data['Interpersonal Skills Rating'],
    final_data['Decision-Making Skills Rating']
)

plt.title('Scatterplot of Interpersonal Skills Rating vs Decision-Making Skills Rating')
plt.xlabel('Interpersonal Skills Rating')
plt.ylabel('Decision-Making Skills Rating')
plt.show()



# plt.figure(figsize=(value_width, value_height))
# sns.heatmap(correlation_matrix, annot=True)        # correlation_matrix : variable that stores the output of the correlation analysis
                                                     # annot=True , If it is True then it will show the correlation coefficient on the map
# plt.title(‘The title of the matrix')
# plt.show()



# Boxplot statistical visualisation method

# plt.figure(figsize=(width, height))
# sns.boxplot(x=‘num_column', y = ‘cat_column', data = data)    # num_column = MANDATORY: numeric column to visualise the boxplot
#                                                               # cat_column = OPTIONAL: categorical column to plot multiple boxplots in one graph
# plt.title(‘The title of the boxplot')
# plt.xlabel(‘The label of the x-axis')
# plt.show() 





