#98 Pandas-3rd
#data frame yapısı bir'den fazla serinin data yapııs içinde toplanması

import pandas as pd
serial1st=[1,3,5,7,9]
serial2nd=[0,2,4,6,8]
#y=pd.Series(serial1st)
#print(y)

headerserial=dict(product1=serial1st,product2=serial2nd)
datas=pd.DataFrame(headerserial)
print(datas)
df=pd.DataFrame([["apple",10],["banana",15],["cherry",20]],columns=["Products","Price"])
print(df)

data2nd=([["apple,10"]["banana",15]["cherry",25]])
header=["Product","Price"]
line=[1,2,3]
df2nd=pd.DataFrame(data2nd,columns=header,index=line)
print(df2nd)

dictnry={"Product":["apple","banana","cherry"],"Price":[10,15,25]}
data=pd.DataFrame(dictnry)
print(data)
