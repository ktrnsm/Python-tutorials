#107 Pandas  DataFrame Join
import pandas as pd
serial1st=pd.DataFrame({
    "City":["istanbul","Ankara","izmir","bursa"],
    "Heat":[15,20,25,30]
})

serial2nd=pd.DataFrame({
    "City":["istanbul","Ankara","izmir","adana"],
    "Heat":["Rainy","Cloudy","Sunny","closed"]
})

result=pd.merge(serial1st,serial2nd,on="City",how="inner") # kesişim kümesini yazdırmaya çalışır.
result2=pd.merge(serial1st,serial2nd,on="City",how="right") # left ilk oluşturulan serinin farkı ile birlikte gelir. 
#right ikinci kümeninkileri getirir.
#outer tamamını dahil eder.
result3=pd.merge(serial1st,serial2nd,on="City",how="outer")
print(result3)