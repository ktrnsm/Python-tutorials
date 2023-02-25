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

#retrun

def sum(x,y):
    res=x+y
    print(res)

sum(3,5)+sum(4,6) # print bunu başaramaz yerine return kullanılmalıdır. iki değişken toplanır ama iki çıktı olmaz

def summ(x,y):
    res=x*y
    return res
summ(6,7)

#arguments in functions

print("ktrn sm", 21,sep="_")

def Sum(x,y,z=0): # birden fazla argümanın girlmesi zorunlu değilse =0 ile verebiliriz.
    result=x+y+z
    return result
print(Sum(4,7))

def Sum(*x): #* demet tuple olarak döndürür
    counter=0
    for i in x:
        counter+=i
    return x
print(Sum(1,3,7,8,9))

def name(*x): # isteğe bağlı keyfi argüman *args yapısı denir.
    return "Hi there this is {}, and {}".format(x[0],x[1])
print(name("ktrn", "sm"))

def cal(**fruit):
    return fruit
print(cal(apple=45,melon=50))

def identity(**info):
    for i in info.keys():
        print(i)
identity(name="ktrn", lastname="sm", age="39")
