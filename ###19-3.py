import pandas as pd
import matplotlib.pyplot as plt
import numpy as bp
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import sklearn.metrics as mt 
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Realestate.csv")
data=original_data.copy()
data.drop(columns=["No","X1 transaction date","X5 latitude","X6 longitude"],axis=1,inplace=True)
data=data.rename(columns={"X2 house age":"house age","X3 distance to the nearest MRT station":"location subway",
                          "X4 number of convenience stores":"location shopping","Y house price of unit area":"house value"})

sns.pairplot(data)
#plt.show()

y=data["house value"]
X=data.drop(columns="house value",axis=1)
pol=PolynomialFeatures(degree=3)
X_pol=pol.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X_pol,y,test_size=0.1,random_state=42)
pol_reg=LinearRegression()
pol_reg.fit(X_train,y_train)
prediction=pol_reg.predict(X_test)
r2=mt.r2_score(y_test,prediction)
Mse=mt.mean_squared_error(y_test,prediction)
print("R2:{} MSE:{}".format(r2,Mse))

