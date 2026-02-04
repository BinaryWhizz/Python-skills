# Class Notes 


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lr_model = LinearRegression()
lr_model.fit(x_reg_train, y_reg_train)

y_lr_pred = lr_model.predict(x_reg_test)

mse_lr = mean_squared_error(y_reg_test, y_lr_pred)
print('MSE: ', mse_lr)



sns.kdeplot(y_lr_pred, label = 'Predicted')
sns.kdeplot(y_reg_test, label = 'Actual')
plt.legend()
plt.show()




from sklearn.tree import DecisionTreeRegressor

dtr_model = DecisionTreeRegressor()
dtr_model.fit(x_reg_train, y_reg_train)

y_dtr_pred = dtr_model.predict(x_reg_test)

dtr_mse = mean_squared_error(y_reg_test, y_dtr_pred)
print('MSE: ', dtr_mse)





sns.kdeplot(y_dtr_pred, label = 'Predicted')
sns.kdeplot(y_reg_test, label = 'Actual')
plt.legend()
plt.show()





from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor()
rf_model.fit(x_reg_train, y_reg_train)

y_rf_pred = rf_model.predict(x_reg_test)

rf_mse = mean_squared_error(y_reg_test, y_rf_pred)
print('MSE:', rf_mse)




sns.kdeplot(y_rf_pred, label = 'Predicted')
sns.kdeplot(y_reg_test, label = 'Actual')
plt.legend()
plt.show()

