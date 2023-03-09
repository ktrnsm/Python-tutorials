#104 Pandas -index changing
import pandas as pd
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx"))
print (data)
#data2=data.set_index("Tc") # değişikliğin kalıcı olup olmadığını belirtmek gerekiyor.
print(data2)
#data.set_index("Tc",inplace=True) # değişikliği yapar.
#data.reset_index() # index'i otomatik arar.
print(data.loc[105])
data.set_index("Tc",inplace=True)
req=int(input("type the id number")) # int yapılması gerekiyor tablo str değil.
print(data.loc[req])

#set index yapısı ile ham veriyi tanımlıyoruz.