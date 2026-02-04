# Class Notes  


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

lgr_model = LogisticRegression()
lgr_model.fit(x_class_train, y_class_train)

y_lgr_pred = lgr_model.predict(x_class_test)

accuracy_lgr = accuracy_score(y_class_test, y_lgr_pred)
print(accuracy_lgr*100,'%')





conf_matrix_lgr = confusion_matrix(y_class_test, y_lgr_pred)

plt.figure(figsize = (12, 6))
sns.heatmap(conf_matrix_lgr, annot = True, fmt = "d", cmap = "Blues")
plt.title('Confusion Matrix for LGR model')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()





from sklearn.tree import DecisionTreeClassifier

dtc_model = DecisionTreeClassifier()
dtc_model.fit(x_class_train, y_class_train)

y_dtc_pred = dtc_model.predict(x_class_test)

accuracy_dtc = accuracy_score(y_class_test, y_dtc_pred)
print(accuracy_dtc*100,'%')





conf_matrix_dtc = confusion_matrix(y_class_test, y_dtc_pred)

plt.figure(figsize = (12, 6))
sns.heatmap(conf_matrix_dtc, annot = True, fmt = "d", cmap = "Blues")
plt.title('Confusion Matrix for DTC model')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()





from sklearn.ensemble import RandomForestClassifier

rfc_model = RandomForestClassifier()
rfc_model.fit(x_class_train, y_class_train)

y_rfc_pred = rfc_model.predict(x_class_test)

accuracy_rfc = accuracy_score(y_class_test, y_rfc_pred)
print(accuracy_rfc*100,'%')





conf_matrix_rfc = confusion_matrix(y_class_test, y_rfc_pred)

plt.figure(figsize = (12, 6))
sns.heatmap(conf_matrix_rfc, annot = True, fmt = "d", cmap = "Blues")
plt.title('Confusion Matrix for RFC model')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

