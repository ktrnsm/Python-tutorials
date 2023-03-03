import requests
from bs4 import BeautifulSoup

for page in range(1,11):

    url="https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(page)
    parser=BeautifulSoup(requests.get(url).content,"html.parser") # kısa şekilde yazılışı

    data=parser.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"})\
    .find_all("div",{"class":"product-list product-list--list-page"})

    for i in data:

        name=i.find("div",{"class":"product-list__content"}).find("a",{"class":"prodcut-list__link"})\
        .find("div",{"class":"product-list__product-name"}).string
        print(name)

        price=i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__cost"})\
        .find("span",{"class":"product-list__price"}).string

        print(f"Phone Model {name.lstrip} Phone Price{price}\n")