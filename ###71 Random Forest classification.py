###71 Random Forest classification

import pandas as pd
import os
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/diabetes.csv")
data=original_data.copy()
y = data["Outcome"]
X = data.drop(columns="Outcome")

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=RandomForestClassifier(random_state=0,criterion="entropy",max_depth=10,min_samples_split=5,n_estimators=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)

acs=accuracy_score(y_test,y_predict)
print(acs*100)


parameters={"criterion":["gini","entropy"],
            "max_depth":([1,2,10]),
            "min_samples_split":[2,5,10],
            "n_estimators":[50,200,500,1000]
            }

#grid=GridSearchCV(model,param_grid=parameters,cv=10,n_jobs=-1)
#grid.fit(X_train,y_train)
#print(grid.best_params_)


#plot_tree(model[0],filled=True,fontsize=5)
importance=pd.DataFrame({"importance":model.feature_importances_},index=X.columns)
importance.sort_values(by="importance",axis=0,ascending=True).plot(kind="barh",color="blue")
plt.title("Variable importance")
plt.show()