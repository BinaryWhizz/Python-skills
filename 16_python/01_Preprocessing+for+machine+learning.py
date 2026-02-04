# Class Notes 


# processed_data.columns



x_reg = processed_data.drop(['CustomerID', 'Gender', 'City', 'Region', 'Purchase_Channel', 'CLV'], axis = 1)
y_reg = processed_data['CLV']




x_class = processed_data.drop(['CustomerID', 'Gender', 'City', 'Region', 'Purchase_Channel', 'Churn_Status'], axis = 1)
y_class = processed_data['Churn_Status']




from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_x_reg = scaler.fit_transform(x_reg)




scaled_x_reg




from sklearn.preprocessing import MinMaxScaler

scaler_2 = MinMaxScaler()
scaled_x_class = (scaler_2.fit_transform(x_class)).round()



scaled_x_class



from sklearn.model_selection import train_test_split

x_reg_train, x_reg_test, y_reg_train, y_reg_test = train_test_split(scaled_x_reg, y_reg, 
                                                                   test_size = 0.2, random_state = 42)



x_reg_test.shape



x_class_train, x_class_test, y_class_train, y_class_test = train_test_split(scaled_x_class, y_class, 
                                                                   test_size = 0.2, random_state = 42)



x_class_train.shape




from sklearn.decomposition import PCA

pca = PCA()
temp_pca = pca.fit_transform(x_reg)
evr = pca.explained_variance_ratio_




plt.figure(figsize = (12, 6))
plt.plot(range(1, len(evr)+1), evr, marker = 'o')
plt.title('PCA plot')
plt.xlabel('Number of Components')
plt.ylabel('EVR')
plt.show()



pca = PCA(n_components = 1)
x_reg_pca = pca.fit_transform(x_reg)

