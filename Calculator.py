print("""  Welcome to Calculator

[1] Addition
[2] Subtraction
[3] Multipilation
[4] Division
[5] Exponention
[q] Exit
""")

Action= input("Please select an action")

if(Action=="1"):
    num1=float(input("first number please"))
    num2=float(input("secound number please"))
    print("Addition result is {}".format(num1+num2))
elif(Action=="2"):
    num1=float(input("first number please"))
    num2=float(input("secound number please"))
    print("Substraction result is {}".format(num1-num2))
elif(Action=="3"):
    num1=float(input("first number please"))
    num2=float(input("secound number please"))
    print("Multipilation result is {}".format(num1*num2))
elif(Action=="4"):
    num1=float(input("first number please"))
    num2=float(input("secound number please"))
    print("Division result is {}".format(num1/num2))
elif(Action=="5"):
    num1=float(input("first number please"))
    num2=float(input("secound number please"))
    print("E result is {}".format(num1**num2))
elif Action =="Q" or Action=="q":
    print("GoodBye")
