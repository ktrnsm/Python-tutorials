#IMDB
import requests
import json
import time
import re
import textwrap

class Movie:
    def __init__(self):
        self.loop=True

    def program(self):
        selection=self.menu()
        
        if selection=="1":
            self.best250()
        if selection=="2":
            self.mostpopular()
        if selection=="3":
            self.now()
        if selection=="4":
            self.soon()
        if selection=="5":
            self.searchmovie()
        if selection=="6":
            self.quit()
    
    def menu(self):
        def control(selection):
            if re.search("[^1-6]",selection):
                raise Exception("select between 1 -6 ")
        while True:
            try:
                selection=input("please decide what to perform \n\n[1]-Best 250\n\n[2]-Most Popular\n\n[3]-Now in Movies\n\n [4]-;Soon \n\n [5]-Search movie\n\n [6]-Quit")
                control(selection)
            except Exception as failure:
                print(failure)
                time.sleep(2)
            else:
                break
        return selection    
        

    def best250(self):
        print(" reacinh to best 250 movies\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_ucfa83zr")
        result = url.json()
        #print(result) herşeyi yazdırır bu bilginin düzenlenmesi gerek 
        for i in result["items"]:
            print(i["fullTitle"])
        self.returnmenu()


    def mostpopular(self):
        print(" reacinh to best most popular\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_ucfa83zr")
        result = url.json()
        #print(result) herşeyi yazdırır bu bilginin düzenlenmesi gerek 
        for i in result["items"]:
            print(i["fullTitle"])
        self.returnmenu()

    def now(self):
        print(" reacinh to novadays\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/InTheaters/k_ucfa83zr")
        result = url.json()
        #print(result) herşeyi yazdırır bu bilginin düzenlenmesi gerek 
        for i in result["items"]:
            print(i["fullTitle"])
        self.returnmenu()
    
    def soon(self):
        print(" reacinh to soon movies\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_ucfa83zr")
        result = url.json()
        #print(result) herşeyi yazdırır bu bilginin düzenlenmesi gerek 
        for i in result["items"]:
            print(i["fullTitle"])
        self.returnmenu()
    
    def searchmovie(self):
        print(" reacing\n\n")
        time.sleep(2)
        film=input("Please type the name of movie")

        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_ucfa83zr")
        result=url.json()
        
        ID=list()
        for i in result["items"]:
            ID.append(i["id"])
        
        NID=list()
        for i in result["items"]:
            NID.append["title"]
        
        flip=zip(NID,ID)
        data=dict(flip)
        key=data.get(film)

        url2=requests.get("https://imdb-api.com/en/API/Wikipedia/k_ucfa83zr/{}".format(key))
        result2=url2.json()
        print(textwrap.fill(result2["plotShort"]["plainText"]),150)
        self.returnmenu()
            
        
        #https://imdb-api.com/en/API/Wikipedia/k_ucfa83zr/tt1375666
    
    def quit(self):
        print("it is exiting")
        time.sleep(2)
        self.loop=False
        exit()
    
    def returnmenu(self):
        while True:
            x=input("Please press 7 for returning to menu or press 6 to exit :")
            if x==7:
                print("returing to main menu")
                time.sleep(2)
                self.program()
                break
            elif x==6:
                self.quit()
                break
            else:
                print("please input a correct value")


System=Movie()
while System.loop:
    System.program()




        