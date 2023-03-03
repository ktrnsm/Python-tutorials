#_83_84 Is investment data scalping
import requests
from bs4 import BeautifulSoup
import time
import re

class Stock:
    def __init__(self):
        self.loop=True


    def program(self):
        
        selection=self.menu()

        if selection=="1":
            time.sleep(2)
            self.presentprice()
        
        if selection=="2":
            time.sleep(2)
            self.coid()

        if selection=="3":
            time.sleep(2)
            self.currentvalue()

        if selection=="4":
            time.sleep(2)
            self.turn()
        
        if selection=="5":
            time.sleep(2)
            self.intindex()
        
        if selection=="6":
            time.sleep(2)
            self.quit()

    
    def menu(self):
        def control(selection):
            if not re.search("[1-6]",selection):
                raise Exception
            elif len(selection)!=1:
                raise Exception
        while True:
            try:
                selection=input("[1]-Actual Price\n[2]Company Details\n[3]-Current Value\n[4]-Annual Turnover\n[5]-internal index\n[6]-Quit")
            except Exception as ex:
                print(ex)
                time.sleep(2)
        return selection


                
    def presentprice(self):
        while True:
            try:
                company=input("Co name")

                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                price=parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}"}.format(company.upper))\
                .parent.parent.find_all("td")
                inf=price[1].string
                inf2=price[2].span.string
                inf3=price[3].string
                inf4=price[4].string
                inf5=price[5].string

                print(f"{inf}\n,{inf2}\n,{inf3}\n,{inf4}\n,{inf5}\n")
                break

            except AttributeError:
                time.sleep(3)
        time.sleep(3)
        self.returnmenu()
    
    def coid(self):
        pass
    
    def currentvalue(self):
        pass

    def turn(self):
        pass
    
    def intindex(self):
        pass

    def quit(self):
        self.loop=False
        exit()


    def returnmenu(self):
        while True:
            x=input("7 or 6")
            if x==7:
                self.program()
                break
            elif x==6:
                self.quit()
                break
            





    
System=Stock()
while System.loop:
    System.program()
        