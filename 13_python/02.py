# Advanced Statistics & Hypothesis Testing 


# Chi square test for independence

# Scenario

# We want to see whether there is any association between customers
# from different regions and purchasing a product from a specific
# purchase channel.

# Hypothesis
# H0: There is no significant association between region and purchase channel.
# Ha: There is a significant association between region and purchase channel.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# Chi-square test for independence

# Performing Test
# from scipy.stats import chi2_contingency
# cross_tab = pd.crosstab(preprocessed_data['Region'], preprocessed_data['Purchase_Channel'])
# chi2, p_value, dof, expected = chi2_contingency(cross_tab)
# print("P-value:", p_value)

# Decision & Conclusion
# alpha = 0.05
# if p_value < alpha:
#  print("Reject the null hypothesis. There is a significant association between region and purchase channel.”)
# else:
#  print("Fail to reject the null hypothesis. There is no significant association between region and purchase channel.”)




# Cross-tabulation test A data has been loaded in the variable final_data. Perform chi-square test for 
# independence to find whether there is any significant association between department and churned variables. 
# Write necessary python code for: Import chi2_contingency python function Perform chi-square test for independence 
# between department and churned variables Keep the output within chi2, p_value, dof, and expected Print the p_value 
# by rounding it up to two decimal points

# import pandas as pd
# import numpy as np
# from scipy import stats

# final_data = pd.read_csv("practice_data.csv", header=0)

# from scipy.stats import chi2_contingency

# Create contingency table
# contingency_table = pd.crosstab(final_data['department'], final_data['churned'])

# Chi-square test for independence
# chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print p-value rounded to two decimal points
# print(round(p_value, 2))



# Pearson correlation analysis

# Scenario
# We want to see whether there is any relationship or correlation
# between frequency of purchases and average purchase amount.

# Hypothesis
# H0: There is no significant relationship between purchase frequency and purchase amount.
# Ha: There is a significant relationship between purchase frequency and purchase amount.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# Pearson correlation
# (If normality assumed)

# Performing Test

# from scipy.stats import pearsonr

# purchase_freq = preprocessed_data[‘Frequency_of_Purchases’]
# purchase_amount = preprocessed_data[‘Average_Purchase_Amount’]
# corr, p_value = pearsonr(purchase_freq, purchase_amount)
# print("P-value:", p_value)

# # Decision & Conclusion

# alpha = 0.05
# if p_value < alpha:
#     print("Reject the null hypothesis. There is a significant relationship between purchase frequency and purchase amount”)
# else:
#     print("Fail to reject the null hypothesis. There is no significant relationship between purchase frequency and purchase amount”)
          


# Pearson correlation
# A data has been loaded in the variable final_data. Perform pearson correlation test to find whether there is 
# any significant relationship between Days Present and Task Completion Rates variables.
# Write necessary python code for:
# Import pearsonr python function
# Load all the values of Days Present variable within the variable DP
# Load all the values of Task Completion Rates variable within the variable TCR
# Perform pearson correlation between DP and TCR
# Keep the output within corr, and p_value
# Print the corr by rounding it up to two decimal points

# import pandas as pd
# import numpy as np
# from scipy import stats

# final_data = pd.read_csv("practice_data.csv", header=0)

# from scipy.stats import pearsonr

# Load variables
# DP = final_data['Days Present']
# TCR = final_data['Task Completion Rates']

# Pearson correlation test
# corr, p_value = pearsonr(DP, TCR)

# Print correlation coefficient rounded to two decimal points
# print(round(corr, 2))


# Linear regression analysis

# Scenario
# We want to see whether the frequency of purchases significantly
# influences customers’ purchase amount.

# Hypothesis
# H0: There is no significant influence of purchase frequency on purchase amount.
# Ha: There is a significant influence of purchase frequency on purchase amount.

# Sig. Level
# 0.05 or 5%

# Appropriate Test
# Linear Regression

# Performing Test

# import statsmodels.api as sm

# x = preprocessed_data[‘Frequency_of_Purchases’]
# y = preprocessed_data[‘Average_Purchase_Amount’]
                      
# x_and_constant = sm.add_constant(x)
# model = sm.OLS(y, x_and_constant ).fit()

# print(model.summary())