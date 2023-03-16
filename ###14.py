###14.1 Multiple linear regression model
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataoperation=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.1.csv")
data=dataoperation.copy()
#print(data)
#print(data.isnull().sum()) # is there any null
#print(data.dtypes) #the all types are what
#print(data.corr()["Sales"]) # sales

#sns.pairplot(data,kind="reg")
#plt.show()

#bulduğumuz iki adet radikal değerin sönümlenmesi
Q1=data["Newspaper"].quantile(0.25)
Q3=data["Newspaper"].quantile(0.75)
IQR=Q3-Q1
upboundary=Q3+1.5*IQR
radicalvalue=data["Newspaper"]>upboundary
data.loc[radicalvalue,"Newspaper"]=upboundary

y=data["Sales"]
X=data[["TV","Radio","Newspaper"]]
stb=sm.add_constant(X)
model=sm.OLS(y,stb).fit()
print(model.summary())
#NewsPaper verlilerinin  sonuçları makül çıkmadığı için onu çıkartıyoruz.

#sns.boxplot(data["TV"]) # aykırı gözlem test ediyoruz.
#sns.boxplot(data["Radio"]) # aykırı gözlem test ediyoruz.
#sns.boxplot(data["Newspaper"]) # aykırı gözlem test ediyoruz. bunda iki adet var.
#plt.show()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#parçalama işlemi gerçekleştirilidi.
lr=LinearRegression()
lr.fit(X_train,y_train)
print(lr.coef_)

prediction=lr.predict(X_test)
y_test=y_test.sort_index()
df=pd.DataFrame({"Reality":y_test,"Prediction":prediction})
df.plot(kind="line")
plt.show()