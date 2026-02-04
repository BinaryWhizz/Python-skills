# Regression Machine Learning 


# Linear regression ML model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mape = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mape) 



# Build Linear Regression ML
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using StandardScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# Train the x_train and y_train within a Linear regression machine learning model.
# Write necessary code for
# Import the function LinearRegression
# Load the function on a variable named lr_model
# Apply the function on the x_train and y_train to fit and train the model

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.linear_model import LinearRegression

# Initialize the Linear Regression model
lr_model = LinearRegression()

# Train the model using training data
lr_model.fit(x_train, y_train)




# Make prediction with LR model
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using StandardScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# A Linear regression machine learning model got trained with x_train and y_train and loaded in a variable lr_model.
# Write necessary code for
# Using the lr_model make the prediction on x_test
# Load the prediction into y_lr_pred
# Print the y_lr_pred 


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

# Make predictions on test data
y_lr_pred = lr_model.predict(x_test)

# Print the predicted values
print(y_lr_pred)




# Evaluate the LR model
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using StandardScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# A Linear regression machine learning model got trained with x_train and y_train and loaded in a variable lr_model.
# Predictions got made and loaded into y_lr_pred
# Write necessary code for
# Import the function mean_squared_error
# Calculate the mean squared error between y_test and y_lr_pred and load the output into mse_lr
# Print the mse_lr by rounding it up to 2 decimal points 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

y_lr_pred = lr_model.predict(x_test)
print(y_lr_pred)

from sklearn.metrics import mean_squared_error

# Calculate Mean Squared Error
mse_lr = mean_squared_error(y_test, y_lr_pred)

# Print MSE rounded to 2 decimal places
print(round(mse_lr, 2))




# Decision tree regressor ML model

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

model = DecisionTreeRegressor()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mape = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mape)




# Decision tree regressor
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using StandardScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# Write necessary code for
# Import the function DecisionTreeRegressor
# Load the function on a variable named dtr_model
# Apply dtr_model on the x_train and y_train to fit and train the model
# Using the dtr_model make the prediction on x_test
# Load the prediction into y_dtr_pred
# Calculate the mean squared error between y_test and y_dtr_pred and load the output into mse_dtr
# Print the mse_dtr by rounding it up to 2 decimal points 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.tree import DecisionTreeRegressor

# Initialize the Decision Tree Regressor
dtr_model = DecisionTreeRegressor(random_state=42)

# Train the model
dtr_model.fit(x_train, y_train)

# Make predictions on test data
y_dtr_pred = dtr_model.predict(x_test)

# Calculate Mean Squared Error
mse_dtr = mean_squared_error(y_test, y_dtr_pred)

# Print MSE rounded to 2 decimal places
print(round(mse_dtr, 2))




# Random forest regressor ML model

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error  

model = RandomForestRegressor()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mape = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mape)




# Random forest regressor
# A prepared data has been loaded in a variable named final_data.
# The features are loaded into x and the target column is loaded into y.
# The features within x got scaled using StandardScaler and loaded into scaled_x.
# The scaled features and target column values got split into train and test data.
# Write necessary code for
# Import the function RandomForestRegressor
# Load the function on a variable named rfr_model
# Apply rfr_model on the x_train and y_train to fit and train the model
# Using the rfr_model make the prediction on x_test
# Load the prediction into y_rfr_pred
# Calculate the mean squared error between y_test and y_rfr_pred and load the output into mse_rfr
# Print the mse_rfr by rounding it up to 2 decimal points 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

final_data = pd.read_csv("practice_data.csv", header=0)
x = final_data.drop('average_performance_score', axis = 1)
y = final_data['average_performance_score']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y, test_size = 0.2, random_state = 42)

from sklearn.ensemble import RandomForestRegressor

# Initialize the Random Forest Regressor
rfr_model = RandomForestRegressor(random_state=42)

# Train the model
rfr_model.fit(x_train, y_train)

# Make predictions on test data
y_rfr_pred = rfr_model.predict(x_test)

# Calculate Mean Squared Error
mse_rfr = mean_squared_error(y_test, y_rfr_pred)

# Print MSE rounded to 2 decimal places
print(round(mse_rfr, 2))
