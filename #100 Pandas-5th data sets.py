 #100 Pandas-5th data sets
from numpy import sqrt, log
import pandas as pd
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/tml.xlsx"))
#print(data[["Kod","Kapanış (TL)"]])
#print(data.loc[0]) # ilk satırı çekiyor.
#print(data.loc[[0,1,2,3,4,5]])
#print(data.loc[5,"Haftalık Getiri (%)"]) # ilk parametre satır, ikincisi sütün
#print(data.loc[0:5,"Haftalık Getiri (%)"])# ilk 5 parametre bilgisini çeker
#print(data.loc[0:5,"Günlük Getiri (%)":"Yıl İçi Getiri (%)"])# : arasındaki sütünları da çeker

#satır veya sütün eklemek

#data["sqrt Price"]=sqrt(data["Kapanış (TL)"])
#print(data)

data.insert(2,column="Log Price",value=(log(data["Kapanış (TL)"])))
print(data)

data2nd=data.drop("Günlük Getiri (%)",axis=1)#sütundan silme için 1 bu orjinal datayı silmez ve işlem yapmaz. kalıcı veya geçici olarak belirtilmesi gerekiyor silme işlemi
print(data2nd)