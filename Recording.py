#user registration automation system
import re
import time

class Record:
    def __init__(self,programname):
        self.programname=programname
        self.loop=True

    def program(self):
        desicion=self.menu()
        if desicion=="1":
            print("Welcome to adding recording menu")
            time.sleep(3)
            self.addrecord()
        if desicion=="2":
            print("Welcome to deleting record menu")
            time.sleep(3)
            self.moverecord()
        if desicion=="3":
            print("we are reacing the records")
            time.sleep(3)
            self.readrecord()


    def menu(self):
        def control(desicion):
            if re.search("[^1-4]",desicion):
                raise Exception("Please make desicion between 1 and 4")
            elif len(desicion!=1):
                raise Exception("Please make desicion between 1 and 4")
        while True:
            try:
                desicion=input(" hi there, {} welcome to our system please decide what to do..\n\n[1] Add Record \n[2]Remove Record\n[3]Read Record \n[4] Exit\n\n".format(self.programname))
                control(desicion)
            except Exception as failure:
                print(failure)
                time.sleep(3)
            else:
                break
        return desicion

        
    def addrecord(self):
        def controlName(Name):
            if Name.isalpha()==False: # alfabetik karakter dışında veri kontrol etmek için kullanılıyor
                raise Exception(" your user name must be a letter")
        while True:
            try:
                Name=input("your name please")
                controlName(Name)
            except Exception as FailureName:
                print(FailureName)
                time.sleep(3)
            else:
                break
        
        def controlLastName(LastName):
            if LastName.isalpha()==False: # alfabetik karakter dışında veri kontrol etmek için kullanılıyor
                raise Exception(" your user name must be a letter")
        while True:
            try:
                LastName=input("your  Last name please")
                controlLastName(LastName)
            except Exception as FailureLastName:
                print(FailureLastName)
                time.sleep(3)
            else:
                break

        def controlAge(Age):
            if Age.isdigit()==False: # alfabetik karakter dışında veri kontrol etmek için kullanılıyor
                raise Exception(" your user name must be a letter")
        while True:
            try:
                Age=input("your age please")
                controlAge(Age)
            except Exception as FailureAge:
                print(FailureAge)
                time.sleep(3)
            else:
                break

        def controlID(ID):
            if ID.isdigit()==False: # alfabetik karakter dışında veri kontrol etmek için kullanılıyor
                raise Exception(" your ID must be a number")
            elif len(ID!=11):
                raise Exception(" it must be 11 long ")
        while True:
            try:
                Age=input("your ID please")
                controlID(Age)
            except Exception as FailureID:
                print(FailureID)
                time.sleep(3)
            else:
                break
            
        def controlEmail(Email):
            if not re.search("@" and ".com",Email):
                raise Exception("Please corret type of Email")
        while True:
            try:
                Email=input("please email")
                controlEmail(Email)
            except Exception as FailureEmail:
                print(FailureEmail)
                time.sleep(3)
            else:
                break




    def moverecord(self):
        pass
    def readrecord(self):
        pass
    def exit(self):
        pass
    def returnToMenu(self):
        pass    



System=Record("ktrn")
while System.loop:
    System.program()