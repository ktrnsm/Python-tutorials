###13 Simple Basic Regression

import pandas as pd
import matplotlib.pylab as plt
import statsmodels.api as sm

operationdata = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###13.csv")
data = operationdata.copy() ## make a copy as always for data and work on it.
#print(data)
#print(data.isnull().sum())
y = data["Salary"]
X = data["YearsExperience"]
#plt.scatter(X, y)
#plt.show()
sbt = sm.add_constant(X)
model = sm.OLS(y, sbt).fit()
print(model.summary())

