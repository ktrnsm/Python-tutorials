#101 Pandas-6th Data frame filtering
import pandas as pd 
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/tml.xlsx"))
print(data.head(15)) # parametresiz ilk 5 satır
print(data.tail(15)) # parametresiz son 5 veriyi verir
print(data["Kapanış (TL)"].head(15)) #seçilen sütunun ilk 15 verisini getirir.
print(data[5:][["Kod"],["Kapanış (TL)"]].head(15)) # 5 ve 15 arasındaki verileri listeler

#veri değerlerine göre filtreleme
print(data=="AEFES")#bu değeri tamamında ara bulursan True dön 
print(data[data=="AEFES"]) #bulduğu yere veriyi yazar bulamazsa NaN olarak işaretler.

#print(data[data>20])#str verinin olduğu yerde int aradığı için hata verir. sütun bazlı yapılması gereklidir.
print(data[data["Günlük Getiri (%)"]>2]) # hata vermeden işler 
filter1st=data[(data["Günlük Getiri (%)"]>2)&(data["Haftalık Getiri (%)"]<1)] # ve
filter2nd=data[(data["Günlük Getiri (%)"]>2)|(data["Haftalık Getiri (%)"]<1)] # veya

print(filter1st)
print(filter2nd)