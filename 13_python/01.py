# Statistics & Hypothesis Testing 

# One sample t-test

# Scenario
# Average purchase amount by the customers in the previous fiscal
# year was USD 68. We want to see whether the customers’ average
# purchasing power increases compared to last year.

# Hypothesis
# H0: There is no significant difference between the average purchase amount and 68.
# Ha: There is a significant difference between the average purchase amount and 68.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# One sample t-test
# (If normality assumed)

# Performing Test

# from scipy import stats
# hypothesis_mean = 68
# t_statistic, p_value = stats.ttest_1samp(data['num_variable'], hypothesis_mean)
# print("P-value:", p_value)

# Decision & Conclusion

# alpha = 0.05
# if p_value < alpha:
#     print("Reject the null hypothesis. There is a significant difference between the average purchase amount and 68.”)
# else:
#     print("Fail to reject the null hypothesis. There is no significant difference between the average purchase amount and 68.)
          


# One sample t-test"
# A data has been loaded in the variable final_data. Perform one sample t-test to find whether there is any significant 
# difference between the average 'Sales Revenue Generated' and the previous average value of 67987.
# Write necessary python code for:
# Import stats python package
# Include the previous average value within hypothesized_mean
# Perform one sample t-test and keep the output within t_stat and p_value
# Print the p_value by rounding it up to two decimal points

# import pandas as pd
# import numpy as np

# final_data = pd.read_csv("practice_data.csv", header=0)

# from scipy import stats

# Hypothesized mean
# hypothesized_mean = 67987

# One-sample t-test
# t_stat, p_value = stats.ttest_1samp(
#     final_data['Sales Revenue Generated'],
#     hypothesized_mean
# )

# Print p-value rounded to 2 decimals
# print(round(p_value, 2))




# Independent sample t-test

# Scenario
# We want to see whether the churned customers spent higher than
# the existing customers based on the average purchase amount.

# Hypothesis
# H0: There is no significant difference in average purchase amount between churned and existing
# customers.
# Ha: There is a significant difference in average purchase amount between churned and existing customers.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# Independent sample t-test
# (If normality assumed)

# Performing Test

# from scipy import stats
# churned = preprocessed_data.query('Churn_Status == "Yes"')['Average_Purchase_Amount']
# existing = preprocessed_data.query('Churn_Status == "No"')['Average_Purchase_Amount']
# t_statistic, p_value = stats.ttest_ind(churned, existing)
# print("P-value:", p_value)

# Decision & Conclusion

# alpha = 0.05
# if p_value < alpha:
#     print("Reject the null hypothesis. There is a significant difference in average purchase amount between churned and existing customers.”)
# else:
#     print("Fail to reject the null hypothesis. There is no significant difference in average purchase amount between churned and existing customers.”)
          



# Two sample t-test
# A data has been loaded in the variable final_data. Perform independent sample t-test to find whether there is any 
# significant difference in the average 'Task Completion Rates' between existing and churned employees.
# Write necessary python code for:
# Filter out all the values of 'Task Completion Rates' for the churned employees and keep it within churned_employee
# Filter out all the values of 'Task Completion Rates' for the existing employees and keep it within existing_employee
# Perform independent sample t-test between churned_employee and existing_employee
# Keep the output within t_stat and p_value
# Print the p_value by rounding it up to two decimal points 

# import pandas as pd
# import numpy as np
# from scipy import stats

# final_data = pd.read_csv("practice_data.csv", header=0)

# Filter Task Completion Rates for churned employees
# churned_employee = final_data[final_data['churned'] == 'Yes']['Task Completion Rates']

# Filter Task Completion Rates for existing employees
# existing_employee = final_data[final_data['churned'] == '’No']['Task Completion Rates']

# Independent two-sample t-test
# t_stat, p_value = stats.ttest_ind(churned_employee, existing_employee)

# Print p-value rounded to two decimal points
# print(round(p_value, 2))



# One way Analysis of Variance

# Scenario
# We want to see whether there is any difference in the average
# frequency of purchases by the customer from various cities.

# Hypothesis
# H0: There is no significant difference in average frequency of purchases among the customers
# from different cities.
# Ha: There is a significant difference in average frequency of purchases among the customers
# from different cities.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# One way ANOVA
# (If normality assumed)

# Performing Test
# from scipy import stats
# Chicago = preprocessed_data.query(‘City == "Chicago"')['Frequency_of_Purchases’]
# New_york = preprocessed_data.query(‘City == ”New York"')['Frequency_of_Purchases’]
# Houston = preprocessed_data.query(‘City == ”Houston"')['Frequency_of_Purchases’]
# Los_angeles = preprocessed_data.query(‘City == ”Los Angeles"')['Frequency_of_Purchases']"

# t_statistic, p_value = stats.f_oneway(Chicago, New_York, Houston, Los_angeles )
# print("P-value:", p_value)

# Decision & Conclusion

# alpha = 0.05

# if p_value < alpha:
#     print("Reject the null hypothesis. There is a significant difference in average frequency of purchases among the customers from different cities.”)
# else:
#     print("Fail to reject the null hypothesis. There is no significant difference in average frequency of purchases among the customers from different cities.”)
          

# Levene's test
# A data has been loaded in the variable final_data. Perform levene's test to find whether there is any 
# significant difference in the variance of Sales Revenue Generated among various levels of Accuracy_of_Work.
# Write necessary python code for:
# Import the python function levene
# Perform levene's test among High, Medium and Low variables' values
# Keep the output within stats and p_value
# Print the p_value by rounding it up to two decimal points

# import pandas as pd
# import numpy as np
# from scipy import stats

# final_data = pd.read_csv("practice_data.csv", header=0)

# High = final_data.query('Accuracy_of_Work == "High"')['Sales Revenue Generated']
# Medium = final_data.query('Accuracy_of_Work == "Medium"')['Sales Revenue Generated']
# Low = final_data.query('Accuracy_of_Work == "Low"')['Sales Revenue Generated']

# from scipy.stats import levene

# Levene's test for equality of variances
# stat, p_value = levene(High, Medium, Low)

# Print p-value rounded to two decimal points
# print(round(p_value, 2))




# Analysis of variance A data has been loaded in the variable final_data. 
# Perform one way ANOVA to find whether there is any significant difference in the average Sales Revenue 
# Generated among various levels of Accuracy_of_Work. Write necessary python code for: Filter out 
# all the values of 'Sales Revenue Generated' for the employees of low accuracy of work and keep it within 
# Low Perform one way ANOVA among High, Medium and Low variables' values Keep the output within 
# Test_stat and p_value Print the p_value by rounding it up to two decimal points

# import pandas as pd
# import numpy as np
# from scipy import stats

# final_data = pd.read_csv("practice_data.csv", header=0)

# High = final_data.query('Accuracy_of_Work == "High"')['Sales Revenue Generated']
# Medium = final_data.query('Accuracy_of_Work == "Medium"')['Sales Revenue Generated']

# Filter Sales Revenue Generated for Low accuracy of work
# Low = final_data.query('Accuracy_of_Work == "Low"')['Sales Revenue Generated']

# One-way ANOVA test
# Test_stat, p_value = stats.f_oneway(High, Medium, Low)

# Print p-value rounded to two decimal points
# print(round(p_value, 2))