###47 Random Forest
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor,RandomForestRegressor
import sklearn.metrics as mt
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()

y=data["Sales"]
X=data.drop(columns="Sales",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)

dt_model=DecisionTreeRegressor(random_state=0)
dt_model.fit(X_train,y_train)
dt_prediction=dt_model.predict(X_test)

dbg_model=BaggingRegressor(random_state=0)
dbg_model.fit(X_train,y_train)
dbg_prediction=dt_model.predict(X_test)

drf_model=RandomForestRegressor(random_state=0)
drf_model.fit(X_train,y_train)
drf_prediction=dt_model.predict(X_test)

r2_dt=mt.r2_score(y_test,dt_prediction)
r2_dbg=mt.r2_score(y_test,dbg_prediction)
r2_drf=mt.r2_score(y_test,drf_prediction)

rmse_dt=mt.mean_squared_error(y_test,dt_prediction,squared=False)
rmse_bg=mt.mean_squared_error(y_test,dbg_prediction,squared=False)
rmse_rf=mt.mean_squared_error(y_test,drf_prediction,squared=False)

#print("Decision Tree:{} RMSE DT :{}".format(r2_dt,rmse_dt))
#print("Bagging:{} RMSE BG:{}".format(r2_dbg,rmse_bg))
#print("Random Forest:{} RMSE RF:{}".format(r2_drf,rmse_rf))

dt_parameters={"min_samples_split":range(2,20)}
dt_grid=GridSearchCV(estimator=dt_model,param_grid=dt_parameters,cv=10)
dt_grid.fit(X_train,y_train)
print(dt_grid.best_params_)
#{'min_samples_split': 10}

bg_parameters={"n_estimators":range(2,20)}
bg_grid=GridSearchCV(estimator=dbg_model,param_grid=bg_parameters,cv=10)
bg_grid.fit(X_train,y_train)
print(bg_grid.best_params_)
#{'n_estimators': 13}

rf_parameters={"max_depth":range(2,20),"max_features":range(2,20),"n_estimators":range(2,20)}
rf_grid=GridSearchCV(estimator=drf_model,param_grid=rf_parameters,cv=10)
rf_grid.fit(X_train,y_train)
print(rf_grid.best_params_)


