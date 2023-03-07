# pandas veri analizinde kullanılır. verinin işlenmsi hazırlanması için idealdir. escel, json,sql farketmez hepsini okuyabilir.
# iki parametresi var.
# seriler(tek boyutlu diziler) ve data frame
import pandas as pd
import numpy as np


serial1st=pd.Series([0,1,2,3,4,5])
serial2nd=pd.Series([0.1,1.16,2.16])
serial3rd=pd.Series(["hi","my","name","is","red"]) # obje olarak döndürür.

print(serial1st)
print(serial2nd)
print(serial3rd)

x=["a",25,"c"]
y=pd.Series(x)
print(y)

a={"apple":2000,"cherry":3000,"banana":4000}
b=pd.Series(a)
print(b)

k=["a","b","c","d",25]
l=pd.Series(k,["x",2,3,4,5]) # index sayısını belirliyoruz.
print(l)

c=np.random.randint(1,500,50)
d=pd.Series(c)
print (d)