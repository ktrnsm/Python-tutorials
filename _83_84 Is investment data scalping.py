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
    
    def coid(self):#company identity information scalping
        while True:
            try:
                company=input("Co name")

                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(company)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                identity=parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}.find_all("tr"))
                for i in identity:
                    inf1=i.th.string
                    inf2=i.td.string
                    print(f"{inf1}:{inf2}")
                break
            except AttributeError:
                time.sleep(3)
        time.sleep(3)
        self.returnmenu()
    
    def currentvalue(self):
        while True:
            try:
                company=input("Co name")

                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(company)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                currentv=parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}.find_all("tr"))
                for i in currentv:
                    inf1=i.th.string
                    inf2=i.td.string
                    print(f"{inf1}:{inf2}\n")
                break
            except AttributeError:
                time.sleep(3)
        time.sleep(3)
        self.returnmenu()

    def turn(self):
        while True:
            try:
                company=input("Co name")

                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(company)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                turn=parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}.find("table")).find("tbody").find_all("tr")

                for i in turn:
                    inf1=i.find_all("td")
                    print(f"Unit:{inf1[0].string} Daily(%):{inf1[1].string} Weekly(%):{inf1[2].string} Monthly(%):{inf1[2].string}Yearly(%):{inf1[3].string}")
                    
                break
            except AttributeError:
                time.sleep(3)
        time.sleep(3)
        self.returnmenu()
    
    def intindex(self):
        while True:
            try:
                company=input("Co name")

                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(company)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                inti=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}.find("table")).find("tbody").find("tr").find_all("td")
                inti2=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}.find("table")).find("thead").find("tr").find_all("th")

                for i in range(0,3):
                    print(f"{inti2[i].string}:{inti[i].string}")
                    
                break
            except AttributeError:
                time.sleep(3)
        time.sleep(3)
        self.returnmenu()

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
        