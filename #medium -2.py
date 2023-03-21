#medium -2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()
#print(data)
#print(data.dtypes)
#print(data.isnull().sum())
#print(data.corr()["Sales"])

#sns.pairplot(data,kind="reg")
#sns.boxplot(data["TV"])
#sns.boxplot(data["Radio"])
Q1=data["Newspaper"].quantile(0.25)
Q3=data["Newspaper"].quantile(0.75)
IQR=Q3-Q1
up_border_limit=Q3+1.5*IQR
outlier=data["Newspaper"]>up_border_limit
data.loc[outlier,"Newspaper"]=up_border_limit
sns.boxplot(data["Newspaper"])
#plt.show()

y=data["Sales"]
X=data[["TV","Radio"]]
constant=sm.add_constant(X)
model=sm.OLS(y,constant).fit()
#print(model.summary())
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#print(X_train)
lr=LinearRegression()
lr.fit(X_train,y_train)
prediction=lr.predict(X_test)
y_test=y_test.sort_index()
data_frame=pd.DataFrame({"Original Value":y_test,"Predicted Value":prediction})
data_frame.plot(kind="line")
plt.show()

