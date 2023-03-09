#106 Pandas excel pulural sheet
import pandas as pd
data2=pd.ExcelFile("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx") # obje olarak tanımlar.
print(data2.sheet_names)
data3=pd.DataFrame(pd.read_excel(data2,sheet_name=data2.sheet_names[2])) #ikinxi indexi getirir.
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx",sheet_name="ill")) 
# sheet_name=2 >> index numarası ile okur.
print(data)
print(data3)

for i in range(0,len(data2.sheet_names)):
    data4=pd.DataFrame(pd.read_excel(data2,sheet_name=data2.sheet_names[i]))
    print(data4)

