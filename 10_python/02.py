# Data Visualisation Methods 

import matplotlib.pyplot as plt
import seaborn as sns 


# bar charts

# .figure() = create a boundary of the visualisation and setting the size of the figure
# .plot() = create the plot or visualisation within the figure
# .title() = assign the title of the figure or graph
# .xlabel() = assign the label in the x-axis
# .ylabel() = assign the label in the y-axis
# .show() = show or visualise the graph


# plt.figure(figsize=(value_width, value_height))
# freq_churned.plot(kind='bar')                      # variable that stores the output of frequency analysis    
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()

# sns.countplot(x = 'Category_col', data = data)



# Bar chart The final data for analysis has been loaded for you within the variable final_data. 
# The frequency analysis has been performed on the variable churned from the given data and stored 
# the output within the variable freq_churned. Write necessary code for the following tasks: 
# Import the required package from matplotlib Define the figure size width = 8 and height = 6 Create a bar plot 
# using the output within freq_churned Assign the title 'Frequencies of churned employees' Assign the x-label 'Churned' 
# Assign the y-label 'Count' Finally, show the plot

import pandas as pd
final_data = pd.read_csv("practice_data.csv", header=0)
freq_churned = final_data['churned'].value_counts()

# Import required package
import matplotlib.pyplot as plt

# Define figure size
plt.figure(figsize=(8, 6))

# Create bar plot using freq_churned
freq_churned.plot(kind='bar')

# Assign title and labels
plt.title('Frequencies of churned employees')
plt.xlabel('Churned')
plt.ylabel('Count')

# Show the plot
plt.show()



# Stacked and clustered bar charts

# plt.figure(figsize=(value_width, value_height))
# cross_tab.plot(kind='bar', stacked=False)        #variable that stores the output of cross tabulation analysis
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()

# sns.countplot(x=' cat_col_1', hue=‘cat_col_2', data=data)



# Clustered bar plot
# The final data for analysis has been loaded for you within the variable final_data. The crosstab analysis has been 
# performed between the variables churned and Accuracy of Work from the given data and stored the output within 
# the variable cross_tab.
# Write necessary code to plot a clustered bar chart using the output within cross_tab.

import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)
cross_tab = pd.crosstab(final_data['churned'], final_data['Accuracy of Work'])


plt.figure(figsize=(8, 6))

cross_tab.plot(kind='bar', stacked=False)

plt.title('Working accuracy level by churned employees')
plt.xlabel('Churned')
plt.ylabel('Count')
plt.show()



# Pie chart for percentage analysis

# plt.figure(figsize=(value_width, value_height))
# percentage.plot(kind='pie', autopct='%1.2f%%’)    # variable that stores the output of percentage analysis , 
                                                    # % - This ensures the percentages are shown on the graph with 
                                                    # two decimal points
# plt.title(‘The title of the graph')
# plt.ylabel(‘ ')
# plt.show()



# Pie chart
# The final data for analysis has been loaded for you within the variable final_data. 
# The percentage analysis has been performed on the variable churned from the given data and stored 
# the output within the variable perc_churned.
# Write necessary code to perform the following tasks:
# Create a pie plot using the output within perc_churned
# Show the decimal number and set it up to 1 point

import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)
freq_churned = final_data['churned'].value_counts()
perc_churned = freq_churned/len(final_data['churned'])*100

plt.figure(figsize=(8, 6))

perc_churned.plot(kind='pie', autopct='%.1f%%', startangle=90)

plt.title('Percentage of churned employees')
plt.ylabel('')
plt.show()



# Line chart

# plt.figure(figsize=(value_width, value_height))
# group_by.plot(kind='line', marker='o’)           # variable that stores the output of group by analysis 
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()

# sns.lineplot(x='cat_col', y='num_col', data=data, marker='o')  

# num_col = numeric column which will be grouped by a numeric measure 
# data=data = variable that stores the entire dataset 
# marker='o' = Marker used to highlight the points in line chart for each categori in category column 



# Line chart
# The final data for analysis has been loaded for you within the variable final_data. 
# The groupby analysis has been performed on the variables department and Sales Revenue Generated from 
# the given data and stored the output within the variable SRG_dept.
# Write necessary code for the following tasks: Create a line plot using the output within 
# SRG_dept Set the marker into 'o' shape

import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)
SRG_dept = final_data.groupby('department')['Sales Revenue Generated'].mean()

plt.figure(figsize=(8, 6))

SRG_dept.plot(kind='line', marker='o')

plt.title('Average sales revenue generated by Employees')
plt.xlabel('Churned')
plt.ylabel('Mean sales revenue')
plt.show()



# Exploring distribution with histogram

# plt.figure(figsize=(value_width, value_height))
# data[num_col'].plot(kind='hist', bins=5)         # deriving the values of the numeric variable
# plt.title(‘The title of the graph')
# plt.xlabel(‘The label of the x-axis')
# plt.ylabel(‘The label of the y-axis')
# plt.show()

# sns.histplot(data[num_col'], bins=5)             # number of bars you want to show within the histogram 



# Histogram The final data for analysis has been loaded for you within the variable final_data. 
# The data includes a variable Task Completion Rates. Write necessary code for the following tasks: Create a histogram 
# using the variable Task Completion Rates Set the number of bins to 5

import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)

plt.figure(figsize=(8, 6))

plt.hist(final_data['Task Completion Rates'], bins=5)

plt.title('Histogram of Task Completion Rates')
plt.xlabel('Task Completion Rates')
plt.ylabel('Frequency')
plt.show()

