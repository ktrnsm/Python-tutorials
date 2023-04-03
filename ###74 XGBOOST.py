###74 XGBOOST
from xgboost import XGBClassifier
import pandas as pd
import os
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
diabetes_data=original_data.copy()

y=diabetes_data["Outcome"]
X=diabetes_data.drop(columns="Outcome",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model_xgb=XGBClassifier(learning_rate=0.2,max_depth=3,n_estimators=500,subsample=0.7)
model_xgb.fit(X_train,y_train)
y_pred=model_xgb.predict(X_test)

model_bay=GaussianNB()
model_bay.fit(X_train,y_train)
y_pred2nd=model_bay.predict(X_test)


acs=accuracy_score(y_test,y_pred)
acs2nd=accuracy_score(y_test,y_pred2nd)
#print(acs2nd*100)
print(acs*100)

parameters={
    "max_depth":[3,5,7],
    "subsample":[0.2,0.5,0.7],
    "n_estimators":[500,1000,2000],
    "learning_rate":[0.2,0.5,0.7]
}

#grid=GridSearchCV(model_xgb,param_grid=parameters,cv=10,n_jobs=-1)
#grid.fit(X_train,y_train)
#print(grid.best_params_)


