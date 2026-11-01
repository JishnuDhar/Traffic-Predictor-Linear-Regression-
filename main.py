## Importing Modules ##
import pandas as pd
import numpy as np 
from sklearn import linear_model

## Reading CSV Files ##
training_data_csv = pd.read_csv('training_data.csv')
testing_data_csv = pd.read_csv('testing_data.csv')

## Defining the regression model used #
reg = linear_model.LinearRegression()

keys = training_data_csv[['Rain_Possibility', 'Important_Festival', 'Weekend', 'Traffic_Last_Year', 'Government_Holiday']].keys

training_data_x_list = training_data_csv[['Rain_Possibility', 'Important_Festival', 'Weekend', 'Traffic_Last_Year', 'Government_Holiday']].values
training_data_y_list = training_data_csv[['Traffic_Possibility']].values

reg.fit(training_data_x_list, training_data_y_list)
# print(f"Coeffs: {reg.coef_}, Intercept: {reg.intercept_}")

testing_data_x_list = testing_data_csv[['Rain_Possibility', 'Important_Festival', 'Weekend', 'Traffic_Last_Year', 'Government_Holiday']].values
testing_data_y_list = testing_data_csv[['Traffic_Possibility']].values

def predict_data(input):
    global reg
    return reg.predict(input)

def check_prediction_variations(predictions, data):
    zipped = zip(predictions.flatten(), data.flatten())
    variations = []
    for a, b in zipped:
        variations.append(abs(a - b))
    ans = 0 
    for k in variations:
        ans += k
    return ans/len(predictions)

# print(predict_data(testing_data_x_list))
# print(check_prediction_variations(predict_data(testing_data_x_list), testing_data_y_list))