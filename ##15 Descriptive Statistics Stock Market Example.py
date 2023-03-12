##15 
import pandas as pd
import matplotlib.pylab as plt

data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/##15Stock.xlsx",usecols=["Erprofit","Clprofit"]))
#print(data.describe())
#print(data.mean())
#print(data.median())
#print(data.quantile(q=0.25)) # 1. kartiller'i getirir.
#print (data.skew())

plt.figure()
plt.title("Stock income value")
plt.hist(data["Erprofit"],color="g",bins=300,histtype="bar")
plt.hist(data["Clprofit"],color="g",bins=300,histtype="bar")
plt.show()