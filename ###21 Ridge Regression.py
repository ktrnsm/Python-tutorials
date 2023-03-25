###21 Ridge Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,RidgeCV
import sklearn.metrics as mt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()
y=data["Sales"]
X=data.drop("Sales",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
lr=LinearRegression()
lr.fit(X_train,y_train)
prediction=lr.predict(X_test)
r2=mt.r2_score(y_test,prediction)
mse=mt.mean_squared_error(y_test,prediction)
#print("R2:{},MSE:{}".format(r2,mse))

ridge_model=Ridge(alpha=0.1)
ridge_model.fit(X_train,y_train)
prediction2nd=ridge_model.predict(X_test)
r2_rid=mt.r2_score(y_test,prediction2nd)
mse_rid=mt.mean_squared_error(y_test,prediction2nd)
#print("R2 Rid:{},MSE Rid:{}".format(r2_rid,mse_rid))

coefficients=[]
lambdas=10**np.linspace(10,-2,100)*0.5
ridge_cv=RidgeCV(alphas=lambdas,scoring="r2")
ridge_cv.fit(X_train,y_train)
print(ridge_cv.alpha_)
for i in lambdas:
    rid_model2nd=Ridge(alpha=i)
    rid_model2nd.fit(X_train,y_train)
    coefficients.append(rid_model2nd.coef_)
#ax=plt.gca()
#ax.plot(lambdas,coefficients)
#ax.set_xscale("log")
#plt.xlabel("Lambda")
#plt.ylabel("Coefficients")
#plt.show()

#sns.heatmap(data.corr(),annot=True)
#plt.show()

