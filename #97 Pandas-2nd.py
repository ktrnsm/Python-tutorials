#97 Pandas-2nd
import pandas as pd
x=pd.Series(["a","b",1],[1,2,3])
print(x)
print(x[[2,3]])

a=pd.Series([1,2,3,4,5])
print(a.sum())
print(a.mean())
print(a.var())
print(a.std())
print(a.kurtosis())

year=[2015,2016,2017,2018,2019,2020,2021,2022,2023]
price=[3,4,5,6,7,8,9,10,11]
serial=pd.Series(year,price)
print(serial)
print(serial.mean()) 
print(serial.median())
print(serial.count())
print(serial.describe())
