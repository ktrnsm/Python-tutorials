###90 Clustering
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?endeks=03#page-1"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")

table=s.find("table",{"id":"summaryBasicData"})
table=pd.read_html(str(table),flavor="bs4")[0]

stocks=[]
for i in table["Kod"]:
    stocks.append(i)
 #print(stocks)

parameters = (
    ("hisse", stocks[0]),
    ("startdate", "06-04-2021"),
    ("enddate", "05-04-2023")
)
url2nd="https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil"
r2=requests.get(url2nd,params=parameters).json()["value"]
data=pd.DataFrame.from_dict(r2)
data=data.iloc[:,0:3]
data=data.rename({"HGDG_HS_KODU":"Stock","HGDG_TARIH":"Date","HGDG_KAPANIS":"Close"},axis=1)

data={"Date":data["Date"],data["Stock"][0]:data["Close"]}
data=pd.DataFrame(data)

del stocks[0]
data_all=[data]
for j in stocks:
    parameters = (
    ("hisse", j),
    ("startdate", "06-04-2021"),
    ("enddate", "05-04-2023")
)
    url2nd="https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil"
    r2=requests.get(url2nd,params=parameters).json()["value"]
    data=pd.DataFrame.from_dict(r2)
    data=data.iloc[:,0:3]
    data=data.rename({"HGDG_HS_KODU":"Stock","HGDG_TARIH":"Date","HGDG_KAPANIS":"Close"},axis=1)

    data={"Date":data["Date"],data["Stock"][0]:data["Close"]}
    data=pd.DataFrame(data)
    data_all.append(data)

#print(data_all)

df=data_all[0]

for last in data_all[1:]:
    df=df.merge(last,on="Date")

data=df.drop(columns="Date",axis=1)

income=data.pct_change().mean()*252
result=pd.DataFrame(income)
result.columns=["Income"]

result["Volality"]=data.pct_change().std()*np.sqrt(252)
result=result.reset_index()
result=result.rename({"index":"Stock"},axis=1)
result.to_csv("C:/Users/Şebnem/Desktop/tutorials/stock.csv",index=False)
