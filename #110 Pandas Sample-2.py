#110 Pandas Sample-2
import pandas as pd
#data=pd.DataFrame(pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/car.csv"))
#data.to_excel("C:/Users/Şebnem/Desktop/tutorials/car2.xlsx",index=False)

data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/car2.xlsx"))
print(data.columns) # stünları indexler
print(data.info()) # data type info
print(len(data.columns))
print(data.head(30)) # ilk 30 ceriyi getiriyor.
print(data.tail(10)) # son 10 adedi getirir.
print(data[100:].head(20)) # 100'den başla 120'ye kadar getir.
print(round(data["Model Yıl"].mean())) # model yılı ortalamasını yuvarlayarak veriyor.

print(data["Km"].min()) # en  düşük km
print(data["Km"].max()) # en yüksek Km
print(data[data["Km"].min()==data["Km"]]) # en düşük km olanları bize listeleyecek.)
print(data.sort_values("Fiyat")) # fiyata göre sılama
print(data.sort_values("Fiyat",ascending=False)) # düşükten yükseğe)
print(data.groupby("Marka")) # markalara göre sıralama
print(data.groupby("Marka").mean().sort_values("Fiyat")["Fiyat"]) # markalara göre fiyat ortamasına göre sıralam

seat=data.groupby("Marka").get_group("Seat")
print(seat.groupby("Arac Tip Grubu").mean()["Fiyat"])
    

