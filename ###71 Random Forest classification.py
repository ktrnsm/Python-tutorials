###71 Random Forest classification

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
data=original_data.copy()
y = data["Outcome"]
X = data.drop(columns="Outcome")

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=RandomForestClassifier(random_state=0)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)

acs=accuracy_score(y_test,y_predict)
print(acs*100)