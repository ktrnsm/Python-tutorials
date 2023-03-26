###26 ElasticNet Regression
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge,Lasso,ElasticNet,ElasticNetCV
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
lasso_model=Lasso(alpha=0.1)
lasso_model.fit(X_train,y_train)
elasticNet_model=ElasticNet(alpha=0.1)
elasticNet_model.fit(X_train,y_train)

print(ridge_model.score(X_train,y_train))
print(lasso_model.score(X_train,y_train))
print(elasticNet_model.score(X_train,y_train))

print(ridge_model.score(X_test,y_test))
print(lasso_model.score(X_test,y_test))
print(elasticNet_model.score(X_test,y_test))

prediction_ridge=ridge_model.predict(X_test)
prediction_lasso=lasso_model.predict(X_test)
prediction_elasticNet=elasticNet_model.predict(X_test)

print(mt.mean_squared_error(y_test,prediction_ridge))
print(mt.mean_squared_error(y_test,prediction_lasso))
print(mt.mean_squared_error(y_test,prediction_elasticNet))
lamb=ElasticNetCV(cv=10,max_iter=10000).fit(X_train,y_train).alpha_
elasticNet_model2nd=ElasticNetCV(alpha=lamb)
print(elasticNet_model2nd.score(X_train,y_train))
print(elasticNet_model2nd.score(X_test,y_test))
prediction_elasticNet2nd=elasticNet_model2nd.predict(X_test)
print(mt.mean_squared_error(y_test,prediction_elasticNet2nd))







