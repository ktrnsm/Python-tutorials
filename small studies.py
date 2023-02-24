User_Name=input("please  enter the user name")
User_Password=input(" please enter your password")

SystemKA= "qwe"
SystemPAS="asd"

if User_Name==SystemKA and User_Password==SystemPAS:
    print("Hi There  {}, Hoşgeldin".format(SystemKA))
elif User_Name!=SystemKA and User_Password!=SystemPAS:
    print("Hi there, User name and password is incorrect")
elif User_Name!=SystemKA:
    print("Hi there user name is not correct")
elif User_Password!=SystemPAS:
    print("Merhaba {}, the passwoed is incorrect".format(SystemKA))


