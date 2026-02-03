# Open the attached csv data file. Open the jupyter notebook environment Go to the folder where the downloaded 
# practice_data.csv is placed Open an ipynb file at that folder Import necessary libraries like pandas, numpy, 
# matplotlib and seaborn Load the csv data file into the jupyter notebook Import the function LabelEncoder Load 
# the function within a variable encoder Perform the label encoding on gender. Apply the encoding on the existing 
# variables' values. Finally, show the first five rows 


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the CSV data file
df = pd.read_csv("practice_data.csv")

# Load LabelEncoder into a variable
encoder = LabelEncoder()

# Perform label encoding on gender column
df['gender'] = encoder.fit_transform(df['gender'])

# Show the first five rows
df.head()


# Questions for this assignment What is the first value of the gender column after performing the label encoding?

# 1 
