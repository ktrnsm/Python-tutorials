#16 Descriptive Statistics Sales Example

import pandas as pd
import matplotlib.pyplot as plt
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/##16.xlsx"))
#print(data.describe())
print(data["Sex"].describe()) # ana bilgi veriyor kadın için detay data çekilmesine izin vermiyor.
print(data["Sex"].value_counts(normalize=True)*100) ##  erkek kadın oranlarını belirtiyor bize.
print(data["Age"].mean())
print(data["Age"].median())
#median ortama ve mod çok yakınsa veri simetrik

#plt.hist(data["Age"],bins=50)
#plt.show()

print(data["Age"].std())#1!in altında dik bir yapıdan bahsederiz. ortalama etrafında yoğunlaşmıştır veri.
print(data["Age"].skew())
print(data["Age"].kurtosis()) # 3 sınırındaysa basıklığın olmadığnı söylüyor. 
print(data["Qty"].kurtosis())
print(data.groupby("Sex").mean())
print(data.groupby("Sex")["Age"].mean())