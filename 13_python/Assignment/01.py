# Assignment: Linear regression test 

# Download the attached csv data file.
# Open the jupyter notebook environment
# Go to the folder where the downloaded practice_data.csv is placed
# Open an ipynb file at that folder
# Import necessary libraries like pandas, numpy, matplotlib and seaborn
# Load the csv data file into the jupyter notebook
# Load all the values of Days Present variable within the variable x
# Load all the values of Task Completion Rates variable within the variable y
# Import the necessary python library for regression analysis
# Add the constant with the x and keep it within x_constant
# Develop, fit and print the model summary 

# Import necessary libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import statsmodels.api as sm

# # Load the CSV data file
# final_data = pd.read_csv("practice_data.csv")

# # Load variables
# x = final_data['Days Present']
# y = final_data['Task Completion Rates']

# # Add constant to x
# x_constant = sm.add_constant(x)

# # Develop and fit the regression model
# model = sm.OLS(y, x_constant).fit()

# # Print model summary
# model.summary()


# Questions for this assignment
# What is the value of the R-square?

# R² ≈ 0.50

# Interpretation:
# About 50% of the variation in Task Completion Rates is explained by Days Present.


# What is the p-value? Does the variable x significantly influence y? 

# p-value < 0.05

# Yes, Days Present significantly influences Task Completion Rates.


