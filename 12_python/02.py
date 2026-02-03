;; Box-cox power transformation method

from scipy.stats import boxcox

def boxcox_transformation(data, column_name):
    transformed_data, _ = boxcox(data[column_name])
    data[f'{column_name}_boxcox'] = transformed_data
    stat, p_value = shapiro(data[f'{column_name}_boxcox'])
    kdeplot = sns.kdeplot(data[f'{column_name}_boxcox'])

    print(kdeplot)
    print('P value: ', p_value)



;; BOXCOX transformation
;; A data has been loaded in the variable final_data.
;; Write necessary python code for:
;; Import boxcox python function
;; Perform boxcox transformation on 'Days Present'
;; Keep the transformed values within transformed_data and the rest into _
;; Include the transformed values in a new column named 'Days Present BOXCOX'
;; Perform the shapiro test for normality and find the p_value of 'Days Present BOXCOX'
;; Finally, print the p_value by rounding the output into 2 decimal points

import pandas as pd
import numpy as np
from scipy.stats import shapiro

final_data = pd.read_csv("practice_data.csv", header=0)

from scipy.stats import boxcox

# Box-Cox transformation
transformed_data, _ = boxcox(final_data['Days Present'])

# Add transformed values to new column
final_data['Days Present BOXCOX'] = transformed_data

# Shapiro-Wilk test for normality
stat, p_value = shapiro(final_data['Days Present BOXCOX'])

# Print p-value rounded to 2 decimal points
print(round(p_value, 2))




;; Yeo-Johnson power transformation method

from scipy.stats import yeojohnson
def yeojohnson_transformation(data, column_name):
    transformed_data, _ = yeojohnson(data[column_name])
    data[f'{column_name}_yeojohnson'] = transformed_data
    stat, p_value = shapiro(data[f'{column_name}_yeojohnson'])
    kdeplot = sns.kdeplot(data[f'{column_name}_yeojohnson'])

    print(kdeplot)
    print('P value: ', p_value)


;; YEO-JOHNSON transformation A data has been loaded in the variable final_data. 
;; Write necessary python code for: Import yeojohnson python function Perform yeojohnson transformation on 
;; 'Days Present' Keep the transformed values within transformed_data and the rest into _ Include the transformed 
;; values in a new column named 'Days Present YEO' Perform the shapiro test for normality and find the p_value of 'Days 
;; Present YEO' Finally, print the p_value by rounding the output into 2 decimal points

import pandas as pd
import numpy as np
from scipy.stats import shapiro

final_data = pd.read_csv("practice_data.csv", header=0)

from scipy.stats import yeojohnson

# Yeo-Johnson transformation
transformed_data, _ = yeojohnson(final_data['Days Present'])

# Add transformed values to new column
final_data['Days Present YEO'] = transformed_data

# Shapiro-Wilk test for normality
stat, p_value = shapiro(final_data['Days Present YEO'])

# Print p-value rounded to 2 decimal points
print(round(p_value, 2))


