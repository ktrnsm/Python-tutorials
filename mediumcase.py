import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###13.csv")
data=original_data.copy()
y=data["Salary"]
X=data["YearsExperience"]
#plt.scatter(X,y)
#plt.show()
constant=sm.add_constant(X)
model=sm.OLS(y,constant).fit()
#print(model.summary())

lr=LinearRegression()
lr.fit(X.values.reshape(-1,1),y.values.reshape(-1,1))
print(lr.coef_,lr.intercept_)
