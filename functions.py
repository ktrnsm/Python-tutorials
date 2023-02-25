#functions
def Sum(x,y):
    result=x+y
    print(result)
Sum(5,7)

print(pow(2,5))#üst alma fonksiyonu

def exp(x,y):
    result=x**y
    print(result)
exp(9,6)

def CalcAge(x):
    age=int(2023-x)
    if age<18:
        print("hi there you are so young".format(age))
    else:
        print("you are aged".format(age))
CalcAge(19)