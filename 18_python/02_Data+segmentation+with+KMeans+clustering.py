# Class Notes 


from sklearn.cluster import KMeans

x = processed_data[['Recency', 'Frequency_Score', 'Monetary_Score']]

wcss = []

for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(x)
    wcss_score = kmeans.inertia_
    wcss.append(wcss_score)




plt.figure(figsize = (12, 6))
plt.plot(range(1, 15), wcss, marker = 'o')
plt.title('Elbow methods')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()



final_km = KMeans(n_clusters = 2)
final_km.fit(x)

labels = final_km.labels_
labels





processed_data['Clusters'] = labels
processed_data.head()





mapping = {0:'Regular customer', 1:'Loyal customer'}
processed_data['Customers_types'] = processed_data['Clusters'].map(mapping)

processed_data.head()

