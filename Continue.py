x="ktrn smh"
for i in x:
    if i==" ":
        break # döngüyü durdurur contiune ara verir
    print(i)

numbCount =2
for i in range(0,3):
    UserName=input("Usr Name")
    UserPass=input("Pass")
    Systemktrn= "ktrn"
    systemsm="123"

    if UserName==Systemktrn and UserPass==systemsm:
        print("You are welcome!")
        break
    elif (UserName!=Systemktrn or UserPass!=systemsm) and numbCount!=0:
        print("wrong answer please try again {}".format(numbCount))
        numbCount=numbCount-1
    else:
        print("Wrong input{} ".format(numbCount))
    