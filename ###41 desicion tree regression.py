###41 desicion tree regression
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import sklearn.metrics as mt

original_data=pd.read_csv("https://raw.githubusercontent.com/mk-gurucharan/Regression/master/IceCreamData.csv")
data=original_data.copy()
#print(data)
y=data["Revenue"]
X=data["Temperature"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=DecisionTreeRegressor(random_state=0,max_leaf_nodes=27,min_samples_split=16)
model.fit(X_train.values.reshape(-1,1),y_train.values.reshape(-1,1))
prediction=model.predict(X_test.values.reshape(-1,1))
#print(prediction)
r2=mt.r2_score(y_test,prediction)
mse=mt.mean_squared_error(y_test,prediction)
print("R2:{} MSE:{}".format(r2,mse))

#parameters={"min_samples_split":range(2,50),"max_leaf_nodes":range(2,50)}
#grid=GridSearchCV(estimator=model,param_grid=parameters,cv=10)
#grid.fit(X_train.values.reshape(-1,1),y_train.values.reshape(-1,1))
#print(grid.best_params_)