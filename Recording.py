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
            elif len(desicion)!=1:
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
            if Age.isdigit()==False: # rakam olup olmadığını kontrol ediyoruz
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
            if ID.isdigit()==False: # rakam olup olmadığını kontrol ediyoruz.
                raise Exception(" your ID must be a number")
            elif len(ID)!=11:
                raise Exception(" it must be 11 long ")
        while True:
            try:
                ID=input("your ID please")
                controlID(ID)
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

        with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","r",encoding="utf-8") as Folder:
            linenumbers=Folder.readlines() # liste biçimine dönüştürür
        if len(linenumbers)==0:
            id=1
        else:
            with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","r",encoding="utf-8") as Folder:
                id=int(Folder.readlines()[-1].split("-")[0])+1 # listenin en son elemanına erişmeki onu parçalamak gerekmekte.
        
        with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","a+",encoding="utf-8") as Folder:
            Folder.write("{}-{} {} {} {} {}\n".format(id,Name,LastName,Age,ID,Email))
            print("your data has been recorded")
        self.returnToMenu()   
      

    def moverecord(self):
        y=input("please type the ID number to remove")
        with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","r",encoding="utf-8") as Folder:
            List=[]
            List2=Folder.readlines()
            for i in range(0,len(List2)):
                List.append(List2[i].split("-")[0])
        del List2[List.index(y)]

        with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","w+",encoding="utf-8") as Folder2:
            for i in List2:
                Folder2.write(i)
            print("record is removing")
            time.sleep(3)
            print("record has beed removed")
            self.returnToMenu()    


    def readrecord(self):
        with open("C:/Users/Şebnem/Desktop/tutorials/records.txt","r",encoding="utf-8") as Folder:
            for i in Folder:
                print(i)
            self.returnToMenu()


        
    def exit(self):
        print("it is exiting")
        time.sleep(3)
        self.loop=False
        exit()
        
    def returnToMenu(self):
        while True:
            x=input("returning to main menu please type 6, for exit type 5")
            if x=="6":
                print(" returing to main menu")
                time.sleep(3)
                self.program()
                break
            elif x=="5":
                self.exit()
                break
            else:
                print("please type a valid selection")
                
Syystem=Record("ktrn")
while Syystem.loop:
    Syystem.program()