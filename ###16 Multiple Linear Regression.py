###16 Multiple Linear Regression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as mt
original_data=sns.load_dataset("tips")
data=original_data.copy()
#print(data)
#print(data.isnull().sum())
#print(data.dtypes)
category=[]
categorical=data.select_dtypes(include=["category"])
for i in categorical.columns:
    category.append(i)

data=pd.get_dummies(data,columns=category,drop_first=True)
y=data["tip"]
X=data.drop(columns="tip",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
lr=LinearRegression()
lr.fit(X_train,y_train)
prediction=lr.predict(X_test)
y_test=y_test.sort_index()
data_frame=pd.DataFrame({"Reality":y_test,"Prediction Value":prediction})
data_frame.plot(kind="line")
plt.show()
print(mt.r2_score(y_test,prediction))