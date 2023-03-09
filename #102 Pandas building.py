#102 Pandas
import pandas as pd
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/building.xlsx"))
#print(data)
#print(data.groupby("ilce_adi").groups) oble olarak tanımladı
district=data.groupby("ilce_adi")
for i in district:
    print(i) #ilçe adına göre gruplanmış olarak döndürüyor.

district2=data.groupby("ilce_adi").get_group("ÜSKÜDAR")
print(district2)

