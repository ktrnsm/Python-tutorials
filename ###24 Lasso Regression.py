###24 Lasso Regression
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge,Lasso,LassoCV
import sklearn.metrics as mt
import numpy as np
housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
data=housing_df.copy()
data["PRICE"]=housing.target
y=data["PRICE"]
X=data.drop(columns="PRICE",axis=1)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
ridge_model=Ridge(alpha=0.1)
ridge_model.fit(X_train,y_train)
prediction=ridge_model.predict(X_test)
#print(ridge_model.score(X_train,y_train))
#print(ridge_model.score(X_test,y_test))
#print(mt.r2_score(y_test,prediction))

lasso_model=Lasso(alpha=0.1)
lasso_model.fit(X_train,y_train)
print(lasso_model.score(X_train,y_train))
print(lasso_model.score(X_test,y_test))
#print(lasso_model.coef_)
#print(ridge_model.coef_)
#print(np.sum(ridge_model.coef_!=0))
#print(np.sum(lasso_model.coef_!=0))

lamb=LassoCV(cv=10,max_iter=10000).fit(X_train,y_train).alpha_
#print(lamb)
lasso_model2nd=Lasso(alpha=lamb)
lasso_model2nd.fit(X_train,y_train)
print(lasso_model2nd.score(X_train,y_train))
print(lasso_model2nd.score(X_test,y_test))