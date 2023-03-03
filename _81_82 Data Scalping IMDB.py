import requests
from bs4 import BeautifulSoup
link="https://www.imdb.com/chart/top/"
connect=requests.get(link)
print(connect) #response 200 bağlantı başarılı

#code=connect.content
#parser=BeautifulSoup(code,"html.parser")

code=requests.get(link).content
parser=BeautifulSoup(code,"html.parser")
tr=parser.find("tbody",{"class":"lister-list"}).find_all("tr")
               
#tbody=parser.find("tbody",{"class":"lister-list"})
#print(tbody)
#tr=tbody.find_all("tr")

#for i in tr:
 #   td=i.find("td",{"class":"titleColumn"})
  #  a=td.find_all("a")
  #  print(a)

for i in tr:
    header=i.find("td",{"class":"titleColumn"}).find("a").string
    print(header)

#print(code) # bütün sayfayı çekti.
