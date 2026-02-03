# Check the excel data file.
# Open the jupyter notebook environment
# Go to the folder where the downloaded boxplot_data.xlsx is placed
# Open an ipynb file at that folder
# Import necessary libraries like pandas, numpy, matplotlib and seaborn
# Load the excel data file into the jupyter notebook
# Create a boxplot for the Task Completion Rates by churned
# Check the lesson of boxplot to get any help


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
data = pd.read_excel("boxplot_data.xlsx")

# Create boxplot for Task Completion Rates by churned
plt.figure(figsize=(6, 4))
sns.boxplot(x="churned", y="Task Completion Rates", data=data)
plt.title("Task Completion Rates by Churn Status")
plt.xlabel("Churned")
plt.ylabel("Task Completion Rates")
plt.show()


# Questions for this assignment
# What is the median Task Completion Rates for the churned employees? 

# Median Task Completion Rate = 80 

