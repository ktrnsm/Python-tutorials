###48 a sample study
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor,RandomForestRegressor
import sklearn.metrics as mt
from sklearn.preprocessing import PolynomialFeatures

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()
#print(data)
y=data["Sales"]
X=data.drop(columns="Sales",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
def model_prediction(model):
    model.fit(X_train,y_train)
    prediction=model.predict(X_test)
    r2=mt.r2_score(y_test,prediction)
    rmse=mt.mean_squared_error(y_test,prediction,squared=False)
    return [r2,rmse]
models=[LinearRegression(),Ridge(),Lasso(),ElasticNet(),SVR(),DecisionTreeRegressor(random_state=0),BaggingRegressor(random_state=0),RandomForestRegressor(random_state=0)]
name=["Linear","Ridge","Lasso","ElasticNet","SVR","DecisionTee", "Bagging","Random Forest"]
result=[]
for i in models:
    result.append(model_prediction(i))
df=pd.DataFrame(name,columns=["Model Name"])
df2nd=pd.DataFrame(result,columns=["R2","RMSE"])
df=df.join(df2nd)
print(df)