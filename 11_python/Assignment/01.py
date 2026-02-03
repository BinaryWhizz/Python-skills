# Check heatmap_data.xlsx file
# Open the jupyter notebook environment Go to the folder where the downloaded heatmap_data.xlsx is placed 
# Open an ipynb file at that folder Import necessary libraries like pandas, numpy, matplotlib and seaborn 
# Load the excel data file into the jupyter notebook Create a correlation matrix using the variables: 
# Task Completion Rates Decision-Making Skills Rating Sales Revenue Generated Take the 3 decimal rounded values and 
# keep the output within a variable Use the variable to create a heatmap Check the lesson of heatmap to get any help 


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
data = pd.read_excel("heatmap_data.xlsx")

# Select required variables
selected_data = data[
    ["Task Completion Rates",
     "Decision-Making Skills Rating",
     "Sales Revenue Generated"]
]

# Create correlation matrix (rounded to 3 decimals)
corr_matrix = selected_data.corr().round(3)

# Display correlation matrix
corr_matrix

# output : 01_output.png



#  Questions for this assignment What is the cell color of the correlation between 'Decision-Making Skills Rating' and 
# 'Sales Revenue Generated'?

# Dark / near-black color

