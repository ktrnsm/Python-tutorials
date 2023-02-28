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
        print("directing to enterance menu")
        time.sleep(2)
        UserName=input("Please type youe name")
        Password=input("please type your password")#login() bu karşılaştırmayı yapacak

        result=self.login(UserName,Password)

        if result==True:
            self.loginsuccess()
        else:
            self.loginfailure()


    def logincontrol(self,UserName,Password):#result içerindeki argümanları almak zorunda
        self.datas=self.getdatas()
        for user in self.datas["Users"]:
            if user["UserName"]==UserName and user["Password"]==Password:
                return True
        return False

    def loginsuccess(self):
        print(" it is checking")
        time.sleep(2)
        print("hi there login is succesfull")
        self.result=False
        self.loop==False

    def loginfailure(self):
        print("UserName or Password is wrong")
        time.sleep(2)
        self.menureturn()

    def enroll(self): 
        def controlus(UserName):
            if len(UserName)<8:
                raise Exception("UserName must be minimum 8")
        while True:
            try:
                UserName=input("Please type your User name")
                controlus(UserName)
            except Exception as failurename:
                print(failurename)
                time.sleep(2)
            else:
                break

        def controlpa(Password):
            if len(Password)<8:
                raise Exception("UserName must be minimum 8")
            elif not re.search("[0-9]",Password):
                raise Exception("there must be min one number in")
            elif not re.search("[A-Z]",Password):
                raise Exception("There must be min one Capital letter")
            elif not re.search("[a-z]",Password):
                raise Exception("There must be a small letter minimum one piece")
        while True:
            try:
                Password=input("Please type your Password")
                controlpa(Password)
            except Exception as failurePass:
                print(failurePass)
                time.sleep(2)
            else:
                break
        def controlEmail(Email):
            if re.search("@" and ".com"):
                raise Exception("please type a correct Email")
        while True:
            try:
                Email=input("your email address please")
                controlEmail(Email)
            except Exception as failureem:
                print(failureem)
                time.sleep(2)
            else:
                break
        result=self.isenrolled(UserName,Email)
        if result==True:
            print("User Name and Email is already exist")
        else:
            activationcode=self.activation()
            status=self.activation(activationcode)
            while True:
                if status==True:
                    self.recorddatas(UserName,Password,Email)
                    break
                else:
                    input("false activation code please type again\n")

    def isenrolled(self,UserName,Email):  # daha önce kayıt var mı kontrolü
        self.datas=self.getdatas()
        #try eklliyoruz kayıt yoksa hatayı engellemek için
        try:
            for user in self.datas["Users"]:
                if user["UserName"]==UserName and user["Email"]==Email:
                    return True
        except KeyError:
            return False
        return False

    def activation(self):
        with open("C:/Users/Şebnem/Desktop/tutorials/activation.txt","w",encoding="utf-8") as Folder:
            activing=str(random.randint(10000,999999))
            Folder.write("your activation code is" + activing)
        return activing

    def activationcontrol(self,activing):
        getactivationcode=input("Please type the activation code")
        if activing==getactivationcode:
            return True
        else:
            return False

    def getdatas(self): # json üzerinden veri almak için kullanılacak
        pass

    def recorddatas(self,UserName,Password,Email):#kayıt işlemini json veritabanına kaydetme işlemi
        pass

    def quit(self):
        print( "good bye")
        time.sleep(2)
        self.loop=False
        exit()

    def menureturn(self):
        while True:
            x=input("for main menu press5 for exit press 4")
            if x==5:
                print("directing to main menu")
                time.sleep(2)
                self.program()
                break
            elif x==4:
                self.quit()
                break
            else:
                print("please decive 5 or 4")

System=Site()
while System.turn:
    System.program()
        