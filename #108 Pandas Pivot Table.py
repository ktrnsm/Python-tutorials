#108 Pandas Pivot Table
import pandas as pd 
import numpy as np
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx"))
#print(data)

data2=data.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=sum)
data3=data.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=np.mean)

data5=data.pivot_table(values="Yas",columns=["Cinsiyet","Kan"],aggfunc=np.mean,index="İl") 


print(data5)