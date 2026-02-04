# Machine Learning Classification 


# Logistic regression ML model

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()




# Build Logistic Regression ML A prepared data has been loaded in a variable named final_data. 
# The features are loaded into x and the target column is loaded into y. The features within x got 
# scaled using MinMaxScaler and loaded into scaled_x. The scaled features and target column values got 
# split into train and test data. Write necessary code for Import the function LogisticRegression 
# Load the function on a variable named lgr_model Apply lgr_model on the x_train and y_train to fit and 
# train the model Using the lgr_model make the prediction on x_test Load the prediction into y_lgr_pred 
# Print the y_lgr_pred 

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('churned', axis = 1)
y = final_data['churned']

scaler = MinMaxScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.linear_model import LogisticRegression

# Initialize the Logistic Regression model
lgr_model = LogisticRegression()

# Train the model
lgr_model.fit(x_train, y_train)

# Make predictions on test data
y_lgr_pred = lgr_model.predict(x_test)

# Print the predicted values
print(y_lgr_pred)





# Evaluate the LGR model
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using MinMaxScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# A Logistic regression machine learning model got trained with x_train and y_train and loaded in a variable lgr_model.
# Predictions got made and loaded into y_lgr_pred
# Write necessary code for
# Import the functions accuracy_score, and confusion_matrix
# Calculate the confusion matrix using y_test and y_lgr_pred. Load the output into conf_matrix_lgr.
# Calculate the accuracy score using y_test and y_lgr_pred. Load the output into accuracy_lgr.
# Print accuracy_lgr multiplying it by 100 and then put '%' 


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('churned', axis = 1)
y = final_data['churned']

scaler = MinMaxScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

lgr_model = LogisticRegression()
lgr_model.fit(x_train, y_train)
y_lgr_pred = lgr_model.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix

# Confusion matrix
conf_matrix_lgr = confusion_matrix(y_test, y_lgr_pred)

# Accuracy score
accuracy_lgr = accuracy_score(y_test, y_lgr_pred)

# Print accuracy in percentage
print(accuracy_lgr * 100, '%')




# Decision tree classification ML model ( DTC Model )

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show() 



# Decision tree classification
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using MinMaxScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# Write necessary code for
# Import the function DecisionTreeClassifier
# Load the function on a variable named dtc_model
# Apply dtc_model on the x_train and y_train to fit and train the model
# Using the dtc_model make the prediction on x_test
# Load the prediction into y_dtc_pred
# Calculate the confusion matrix using y_test and y_dtc_pred. Load the output into conf_matrix_dtc.
# Calculate the accuracy score using y_test and y_dtc_pred. Load the output into accuracy_dtc.
# Print accuracy_dtc multiplying it by 100 and then put '%' 

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('churned', axis = 1)
y = final_data['churned']

scaler = MinMaxScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.tree import DecisionTreeClassifier

# Initialize the Decision Tree Classifier
dtc_model = DecisionTreeClassifier(random_state=42)

# Train the model
dtc_model.fit(x_train, y_train)

# Make predictions on test data
y_dtc_pred = dtc_model.predict(x_test)

# Confusion matrix
conf_matrix_dtc = confusion_matrix(y_test, y_dtc_pred)

# Accuracy score
accuracy_dtc = accuracy_score(y_test, y_dtc_pred)

# Print accuracy in percentage
print(accuracy_dtc * 100, '%')





# Random forest classification ML model ( RFC model )

from sklearn.tree import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()




# Random forest classification
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using MinMaxScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# Write necessary code for
# Import the function RandomForestClassifier
# Load the function on a variable named rfc_model
# Apply rfc_model on the x_train and y_train to fit and train the model
# Using the rfc_model make the prediction on x_test
# Load the prediction into y_rfc_pred
# Calculate the confusion matrix using y_test and y_rfc_pred. Load the output into conf_matrix_rfc.
# Calculate the accuracy score using y_test and y_rfc_pred. Load the output into accuracy_rfc.
# Print accuracy_rfc multiplying it by 100 and then put '%'. 

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('churned', axis = 1)
y = final_data['churned']

scaler = MinMaxScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.ensemble import RandomForestClassifier

# Initialize the Random Forest Classifier
rfc_model = RandomForestClassifier(random_state=42)

# Train the model
rfc_model.fit(x_train, y_train)

# Make predictions on test data
y_rfc_pred = rfc_model.predict(x_test)

# Confusion matrix
conf_matrix_rfc = confusion_matrix(y_test, y_rfc_pred)

# Accuracy score
accuracy_rfc = accuracy_score(y_test, y_rfc_pred)

# Print accuracy in percentage
print(accuracy_rfc * 100, '%')



