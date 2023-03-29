###42 Bagging desicion Tree
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import sklearn.metrics as mt
from sklearn.ensemble import BaggingRegressor
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()
y=data["Sales"]
X=data.drop(columns="Sales",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
dtmodel=DecisionTreeRegressor(random_state=0,max_leaf_nodes=18,min_samples_split=4)
dtmodel.fit(X_train,y_train)
dt_prediction=dtmodel.predict(X_test)
r2=mt.r2_score(y_test,dt_prediction)
rmse=mt.mean_squared_error(y_test,dt_prediction,squared=False)
print("Desicion Tree R2:{} Desicion Tree RMSE:{}".format(r2,rmse))
bg_model=BaggingRegressor(random_state=0,n_estimators=23)
bg_model.fit(X_train,y_train)
bg_prediction=bg_model.predict(X_test)
r2_2nd=mt.r2_score(y_test,bg_prediction)
rmse_2nd=mt.mean_squared_error(y_test,bg_prediction,squared=False)
print("Bagging R2:{} Bagging RMSE:{}".format(r2_2nd,rmse_2nd))

#parameters_1st={"min_samples_split":range(2,25),"max_leaf_nodes":range(2,25)}
#grid1st=GridSearchCV(estimator=dtmodel,param_grid=parameters_1st,cv=10)
#grid1st.fit(X_train,y_train)
#print(grid1st.best_params_)

#parameters_2nd={"n_estimators":range(2,25)}
#grid2nd=GridSearchCV(estimator=bg_model,param_grid=parameters_2nd,cv=10)
#grid2nd.fit(X_train,y_train)
#print(grid2nd.best_params_)


