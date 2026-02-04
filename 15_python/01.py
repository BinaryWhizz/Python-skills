# Selecting features and target 

# x = data.drop([‘col_1’, ‘col_2’, …. ], axis=1)
# y = data['target_column']


# Feature selection
# A prepared data has been loaded in a variable named final_data. You will select and separate 
# the features and target columns as instructed below:
# Write necessary code for
# Drop the target column average_performance_score from the data and load all other features into x
# Derive all the values of the target column average_performance_score within y 

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)

# Separate features and target
x = final_data.drop(columns=['average_performance_score'])
y = final_data['average_performance_score']




# Scaling features - StandardScaler

# from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# scaled = scaler.fit_transform(features)        # features : Variable that contains only the features 
                                                 # fit_transform : Method to fit the standardscaler and transform the values of features into scaled values



# Standard scaling
# A prepared data has been loaded in a variable named final_data. The features are 
# loaded into x and the target column is loaded into y. You will scale the features using StandardScaler.
# Write necessary code for
# Import the function StandardScaler
# Load the function within variable scaler
# Apply the function on the variable x and load the output in scaled_x

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

from sklearn.preprocessing import StandardScaler

# Initialize the scaler
scaler = StandardScaler()

# Apply standard scaling on features
scaled_x = scaler.fit_transform(x)




# Scaling features - MinMaxScaler

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled = scaler.fit_transform(features)           # features : Variable that contains only the features 
                                                  # fit_transform : Method to fit the MinMaxScaler and transform the values of features into scaled values 0 and 1




# MinMax scaling
# A prepared data has been loaded in a variable named final_data. 
# The features are loaded into x and the target column is loaded into y. You will scale the features using MinMaxScaler.
# Write necessary code for
# Import the function MinMaxScaler
# Load the function within variable scaler
# Apply the function on the variable x and load the output in scaled_x


import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

from sklearn.preprocessing import MinMaxScaler

# Initialize the scaler
scaler = MinMaxScaler()

# Apply Min-Max scaling on features
scaled_x = scaler.fit_transform(x)




# Dimensionality reduction with PCA

from sklearn.decomposition import PCA 

pca = PCA()
temp_pca = pca.fit_transform(x)
evr = pca.explained_variance_ratio_                     # explained_variance_ratio_  = Method to find the variance ratio for each component/feature

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(evr) + 1), evr, marker='o')
plt.title('Explained Variance Ratio')                 
plt.xlabel('Number of Components')
plt.ylabel('Explained Variance Ratio')
plt.show()



# Explained variance ratio
# A prepared data has been loaded in a variable named final_data. 
# The features are loaded into x and the target column is loaded into y. You will calculate the explained 
# variance ratio by applying principal component analysis.
# Write necessary code for
# Import the function PCA
# Load the function within variable pca
# Apply the pca on the variable x and load the output in temp_pca
# Derive the explained variance ratios from the pca and load it in evr 

import pandas as pd
import numpy as np

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

from sklearn.decomposition import PCA

# Initialize PCA
pca = PCA()

# Apply PCA on the feature set
temp_pca = pca.fit_transform(x)

# Extract explained variance ratios
evr = pca.explained_variance_ratio_




# Select n_component
# A prepared data has been loaded in a variable named final_data. The features are loaded into x and the target 
# column is loaded into y. The explained variance ratios are calculated and loaded in evr.
# Write necessary code for
# Call the method plot from plt
# Add the range of components
# Add the calculated explained variance ratios
# Set the marker type 'o'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

pca = PCA()
temp_pca = pca.fit_transform(x)
evr = pca.explained_variance_ratio_

plt.figure(figsize = (12, 6))

plt.plot(range(1, len(evr) + 1), evr, marker='o')

plt.title('PCA plot')
plt.xlabel('Number of Components')
plt.ylabel('EVR')
plt.show()



# Principal component analysis
# A prepared data has been loaded in a variable named final_data. The features are loaded into x and 
# the target column is loaded into y. You will perform principal component analysis to derive 2 components.
# Write necessary code for
# Load the function PCA within variable pca
# Ensure the number of components become 2
# Apply the pca on the variable x and load the output in x_pca

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

# Initialize PCA with 2 components
pca = PCA(n_components=2)

# Apply PCA on the feature set
x_pca = pca.fit_transform(x)



# Splitting into train and test set 

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(scaled, y, test_size=0.2, random_state=42) 

# scaled = scaled features will be added not th actual features and values
# test_size = Here 0.2 indicates that 20% of the data will be considered as test data and 80% will be train data
# random_state = Assigning a random value to keep consistency in the splitting of the data 



# Train test split
# A prepared data has been loaded in a variable named final_data. The features are loaded 
# into x and the target column is loaded into y. The features within x got scaled using StandardScaler and 
# loaded into scaled_x. You will split the scaled features and target column values into train and test data.
# Write necessary code for
# Import the function train_test_split
# Apply the function on scaled_x and y. Keep the size of the test data 20% and the rand state value 42.
# Load the output into x_train, x_test, y_train, and  y_test 


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    scaled_x, y, test_size=0.2, random_state=42
)
