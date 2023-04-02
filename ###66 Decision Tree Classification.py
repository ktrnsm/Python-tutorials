###66 Decision Tree Classification
import pandas as pd
import os
os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/cancer_data.csv")
data=original_data.copy()
data=data.drop(columns=["id","Unnamed: 32"],axis=1)

data.diagnosis=[1 if code=="M" else 0 for code in data.diagnosis]
y=data["diagnosis"]
X=data.drop(columns="diagnosis",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=DecisionTreeClassifier(random_state=0,criterion="gini",max_depth=6,min_samples_leaf=3,min_samples_split=2)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
acs=accuracy_score(y_test,prediction)
#print(acs*100)

xname=list(X.columns)
#plot_tree(model,filled=True,fontsize=9,feature_names=xname)
#plt.show()


parameters={"criterion":["gini","entropy","log_loss"],"max_leaf_nodes":range(2,10),
            "max_depth":range(2,10),"min_samples_leaf":range(2,10),"min_samples_split":range(2,10)}

grid=GridSearchCV(model,param_grid=parameters,cv=10,n_jobs=-1)
grid.fit(X_train,y_train)
print(grid.best_params_)
