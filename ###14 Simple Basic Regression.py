###14 Simple Basic Regression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

operationaldata=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###13.csv")
data=operationaldata.copy()

y=data["Salary"]
X=data["YearsExperience"]
lr=LinearRegression()
lr.fit(X.values.reshape(-1,1),y.values.reshape(-1,1))
print(lr.intercept_,lr.coef_)
print(lr.predict(X.values.reshape(-1,1)))

# parametreleri teker teker çağılırması gerekiyor. stats gibi toplu gösterim yapmıyor.
