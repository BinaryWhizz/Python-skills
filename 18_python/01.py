# Clustering Machine Learning 


from sklearn.cluster import KMeans

x = processed_data[['Recency', 'Frequency_Score', 'Monetary_Score']] 

WCSS = []

for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(x)
    WCSS_score = kmeans.inertia_
    WCSS.append(WCSS_score) 



# Calculating WCSS
# A data has been loaded into the variable final_data. You will use this data to cluster 
# employees into a certain segments. Now, you will calculate the WCSS scores following the instructions given.
# Write necessary python code for
# Import the function KMeans
# Create a blank list and load it into a variable wcss
# Create a for loop. Consider each value of cluster as i from a range between 1 and 15
# Use the function  KMeans and set the necessary values for the attributes n_clusters and init. 
# Load the function within a variable kmeans
# Use kmeans to fit the final_data
# Find the WCSS scores from kmeans and load into a variable wcss_score
# Finally, append the wcss_score into the blank list wcss 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

final_data = pd.read_csv("practice_data.csv", header=0)

from sklearn.cluster import KMeans

# Create an empty list to store WCSS values
wcss = []

# Loop through number of clusters from 1 to 14
for i in range(1, 15):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(final_data)
    
    # Get WCSS score
    wcss_score = kmeans.inertia_
    
    # Append WCSS score to list
    wcss.append(wcss_score)




# electing optimal number of clusters

from sklearn.cluster import KMeans

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++')
    kmeans.fit(x)
    wcss_values = kmeans.inertia_
    wcss.append(wcss_values )

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



# Plotting Elbow chart
# A data has been loaded into the variable final_data. You will use this data to cluster employees 
# into a certain segments. The WCSS scores are also calculated and loaded into the variable wcss.
# Write necessary python code for plotting the elbow chart for each wcss score by its correspondent number of cluster. 
# The range of number will be between 1 and 15. Set the market style as 'o' 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

final_data = pd.read_csv("practice_data.csv", header=0)

wcss = []

for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(final_data)
    wcss_score = kmeans.inertia_
    wcss.append(wcss_score)

plt.figure(figsize = (12, 6))

plt.plot(range(1, 15), wcss, marker='o')

plt.title('Elbow methods')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()




# Application of KMeans machine learning

kmeans = KMeans(n_clusters= selected_k_value)
kmeans.fit(x)
labels = kmeans.labels_ 



# Building KMeans cluster
# A data has been loaded into the variable final_data. You will use this data to cluster employees 
# into a certain segments. The WCSS scores are also calculated and loaded into the variable wcss. 
# And after plotting the elbow chart, we got 2 as the optimal number of clusters.
# Write necessary python code for
# Use the function  KMeans and set the necessary values for the attribute n_clusters. 
# Load the function within a variable final_km
# Use final_km to fit the final_data
# Derive the labels of the clusters final_km and load it into a variable labels
# Print the labels 

import pandas as pd
from sklearn.cluster import KMeans

# Load data
final_data = pd.read_csv("practice_data.csv", header=0)

# Build final KMeans model with strict limits
final_km = KMeans(
    n_clusters=2,
    init='k-means++',
    n_init=1,
    max_iter=100,
    random_state=42
)

# Fit the model
final_km.fit(final_data)

# Get cluster labels
labels = final_km.labels_

# Print labels
print(labels)
