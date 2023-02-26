class Customer:
    def __init__(self,name,lastname,balance,dept,lastdate, password):
        self.name=name
        self.lastname=lastname
        self.balace=balance
        self.dept=dept
        self.lastdate=lastdate
        self.password=password

Ktrn=Customer("ktrn","sm",4000,2500,12/10/2023,"1234")
Sm=Customer("sm","ktrn",75000,45000,12/10/2023,"4567")


inserted=Ktrn


class ATM:
    def __init__(self,AtmName):
        self.AtmName=AtmName
        self.control()
        self.loop=True
    
    def control(self):
        turn=2
        for i in range(0,3):
            Password=input("pasword please")
            if Password==inserted.password:
                self.program()
            elif Password!=inserted.password and turn!=0:
                print("wrong password try again your left tur is {}".format(turn))
            elif Password!=inserted.password and turn==0:
                print("your card is blocked")
                exit()
    def program(self):
        pick=self.menu()
        if pick==1:
            self.Accbalance()
        if pick==2:
            self.carddept()
        if pick==3:
            self.cashout()
        if pick==4:
            self.cashin()
        if pick==5:
            self.quit()

    def menu(self):
        pick=int(input("**** hi {} dear {} {}.\n\n decide what to do \n\n[1] balance\n[2] dept\n[3] cashout \n[4] cashin\n[5] exit\n desicion:".format(self.AtmName,inserted.name,inserted.lastname)))
        while pick<1 or pick>5:
            print("between 1 and 5 please\n direcitng to main menu")
            self.program()
        return pick
    def Accbalance(self):
        print("account  balance is {}".format(inserted.balace))
        self.loop=False
        self.menureturn()
        
    def carddept(self):
        print("account dept is {} and the last date is {}".format(inserted.dept,inserted.lastdate))
        self.loop=False
        self.menureturn()

    def cashout(self):
        qty=int(input("please tpye your cashout value"))
        newqty=inserted.balace-qty
        if(qty>inserted.balace):
            print("low balance")
            self.menureturn()
        else:
            print("please check the casout the new balance is {}".format(newqty))
            self.menureturn()

        
    def cashin(self):
        qty2=int(input(" please type the amount"))
        newqty2=inserted.balace+qty2
        print("the new balance is {}".format(newqty2))
        self.menureturn()
    
    def quit(self):
        print("goodBye")
        exit()
        
    def menureturn(self):
        x=int(input("for main menu please 7 return of card press 5"))
        if x==7:
            self.program()
        elif x==5:
            self.quit()


Bank=ATM("KTRNBANK")
while Bank.loop:
    Bank.program()


        
            