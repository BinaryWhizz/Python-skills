
# Check practice_data.xlsx
# Open the jupyter notebook environment
# Go to the folder where the downloaded practice_data.xlsx is placed
# Open an ipynb file at that folder
# Import necessary libraries like pandas, numpy, matplotlib and seaborn
# Load the excel data file into the jupyter notebook 
# Create two kdeplots within one figure for Days Present and Sales Revenue Generated
# Use the row num = 1 and column num = 2
# Figure width = 12 and height = 6
# Plot the graphs


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel data file
data = pd.read_excel("practice_data.xlsx")

# Create a figure with 1 row and 2 columns
plt.figure(figsize=(12, 6))

# KDE plot for Days Present
plt.subplot(1, 2, 1)
sns.kdeplot(data["Days Present"])
plt.title("KDE Plot of Days Present")

# KDE plot for Sales Revenue Generated
plt.subplot(1, 2, 2)
sns.kdeplot(data["Sales Revenue Generated"])
plt.title("KDE Plot of Sales Revenue Generated")

# Display the plots
plt.tight_layout()
plt.show()



# Questions for this assignment
# What is the range of highest number of sales revenue generated? 

# 70,000 to 90,000 




