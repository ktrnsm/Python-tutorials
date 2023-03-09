#105 Pandas  NaN values
import pandas as pd
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx"))
#boş olmayan değerleri NaN olarak döndürülür.
print(data.isnull()) # boş değerleri True döndürür olanları false tersi sorgu null tersini yapar.
print(data.isnull().sum()) #tabloda NaN değer kaçar adet olduğunu bulur.
#Nan değer olan satır sütun silimi
data2=data.dropna(axis=1) # sütun içerisinde siler. Nan değer olan sütunu komple siler
data3=data.dropna(subset=["Cinsiyet","Yas","İlce"]) # sadece bu sütun(lar) üzerindeki boş verileri siler.
print(data2)

data4=data.fillna(value="No values") #NaN yerine yazılanı koyar