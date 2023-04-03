###77 Lighgmb

from lightgbm import LGBMClassifier
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import os

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
diabetes_data=original_data.copy()
y=diabetes_data["Outcome"]
X=diabetes_data.drop(columns="Outcome",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
model=LGBMClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
acs=accuracy_score(y_test,y_pred)
print(acs*100)

parameters={
    "learning_rate":[0.001,0.01,0.1],
    "max_depth":[3,5,7],
    "subsample":[0.6,0.8,1]
}
grid=GridSearchCV(model,param_grid=parameters,cv=10,n_jobs=-1)
grid.fit(X_train,y_train)
print(grid.best_params_)




