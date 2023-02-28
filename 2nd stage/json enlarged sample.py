import json
import re
import time
import random
#json yapısını veri işleme veri kazıma için kullanacağız.
#fonkiyona parametre göndererk prje yapılacak

class Site:
    def __init__(self):
        self.turn=True
        self.datas=self.getdatas()

    def program(self):# ekrana menü yazdıracak
        selection=self.menu()
        if selection=="1":
            self.login()
        if selection=="2":
            self.enroll()
        if selection=="3":
            self.quit()

    def menu(self):# 1 ve 3 dışında seçenek seçilmemesi için kontrol kuruyoruz.
        def kontrol(selection):
            if re.search("[^1-3]",selection):
                raise Exception("Please select between 1-3")
            elif len(selection)!=1:
                raise Exception("please insert valid single number")
        while True:
                try:
                    selection=input("hi there my name is red\n\n Please select the application\n\n[1]-Enter\n[2]-Enroll\n[3]-Exit\n\n")
                    kontrol(selection)
                except Exception as failure:
                    print(failure)
                    time.sleep(2)
                else:
                    break
        return selection
            
        

    def login(self):
        pass

    def logincontrol(self):
        pass

    def loginsuccess(self):
        pass

    def loginfailure(self):
        pass

    def enroll(self): 
        pass

    def isenrolled(self):  # daha önce kayıt var mı kontrolü
        pass

    def activation(self):
        pass

    def activationcontrol(self):
        pass

    def emailcheck(self):
        pass

    def getdatas(self): # json üzerinden veri almak için kullanılacak
        pass

    def recorddatas(self):#kayıt işlemini json veritabanına kaydetme işlemi
        pass

    def quit(self):
        pass

    def menureturn(self):
        pass

System=Site()
while System.turn:
    System.program()
        