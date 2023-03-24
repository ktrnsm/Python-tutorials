###19.2 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn 

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Realestate.csv")
data=original_data.copy()

data.drop(columns=["No","X6 longitude","X5 latitude","X1 transaction date"],axis=1,inplace=True)
#print(data.info())
#sns.pairplot(data)
#plt.show()

y=data["Y house price of unit area"]
X=data.drop(columns="Y house price of unit area",axis=1)
#print(X)



