###78
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/WA_Fn-UseC_-Telco-Customer-Churn.csv")
data=original_data.copy()
data=data.drop(columns="customerID",axis=1)
data["TotalCharges"]=pd.to_numeric(data["TotalCharges"],errors="coerce")


def predict_missing_total_charges(data):
    missing_mask = data['TotalCharges'].isnull()
    missing_X = data.loc[missing_mask, ['MonthlyCharges', 'tenure']].values
    non_missing_X = data.loc[~missing_mask, ['MonthlyCharges', 'tenure']].values
    non_missing_y = data.loc[~missing_mask, 'TotalCharges'].values
    model = LinearRegression()
    model.fit(non_missing_X, non_missing_y)
    missing_y_pred = model.predict(missing_X)
    data.loc[missing_mask, 'TotalCharges'] = missing_y_pred
    return data
data = predict_missing_total_charges(data)
print(data.isnull().sum())



