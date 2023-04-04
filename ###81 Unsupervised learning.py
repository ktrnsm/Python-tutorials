### extra
import requests
from bs4 import BeautifulSoup
import pandas as pd

stocks=[]
url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ACSEL"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
sl=s.find("select",id="ddlAddCompare")
cl=sl.findChild("optgroup").findAll("option")
