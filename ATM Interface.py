print("""\t ********Hi There welcome to yourbank*********
\t\t Please insert your card
""")

Database={"MyAccount":{
    "Name":"ktrn",
    "LastName":"sm",
    "CardPass":"1234",
    "AccountBalance":1000,
    "AccountDept":4200,
    "DeptCardDeptDate":20/11/2021
},
"YourAccount":{
    "Name":"smh",
    "LastName":"ktrn",
    "CardPass":"4567",
    "AccountBalance":2000,
    "AccountDept":4000,
    "DeptCardDeptDate":20/12/2021
}}

insertedCArd=dict(Database["MyAccount"])

turn=2
for i in range(0,3):
    Password=input("Please type your 4 letter Password")
    if Password==insertedCArd.get("CardPass"):
        print("""Hi there  dear {} {}
        Please do what you want """.format(insertedCArd.get("Name"),insertedCArd.get("LastName")))
        pick=input("""
         [1] Check the Balance
         [2] Check the Dept
         [3] Get Cash
         [4] Set Cash
         [Q] Return Card\n """)
        break
    elif Password!=insertedCArd.get("CardPassword") and turn!=0:
        print("Incorrect Password. your turn is {} ".format(turn))
        turn-=1
    elif Password!=insertedCArd.get("CardPasword") and turn==0:
        print("""Your card is blocked due to 3 times wrong typing
        Please Communicate with the closest bank office""")
        exit() # program akışının devamı için gereklidir.
if pick==1:
    print("AccountBalance is {}".format(insertedCArd.get("AccountBalance")))
elif pick==2:
    print("AccountDept is {} the last payment date is {}".format(insertedCArd.get("AccountDept"),insertedCArd.get("DeptCardDeptDate")))
elif pick==3:
    qty=int(input("Please type the requested cash value"))
    if(insertedCArd.get("AccountBanace")<qty):
        print("The enough balance to cash out")
    else:
        print("Please take your cash out carefully")
        newbalance=insertedCArd.get("AccountBalance"-qty)
        print(" the remaining balance in {}".format(newbalance))
elif pick==4:
    qty2=int(input("Please type your wished cash in"))
    newbalance2=insertedCArd.get("AccountBalance")+qty2
    print("The cash i is succesfully in ")
    print("The remaining balance is {}".format(newbalance2))
else:
    print("Please type make sense information")