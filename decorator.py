#decorator
def Sum(x,y):
    result=x+y
    print(result)
Sum(4,6)

a=Sum # fonskiyonu değişkene atma
a(4,8)

def func1():
    print("Hi There")

    def func2():
        return "all is well"
    print(func2())
func1()


def function1(func):
    def wrapper():
        print("addtional area One")
        func()
        print("additional area Two")
    return wrapper

@function1
def hi():
    print("hi there")

hi()

def deco(func):
    def wrapper(x,y):
        print("... the result is")
    return wrapper
@deco
def Sum(x,y):
    result=x+y
    print(result)
@deco
def Mulp(x,y):
    result=x*y
    print(result)

Sum(4,6)
Mulp(4,6)




import time

def Sum(x,y):
    start=time.time()
    time.sleep(2)
    result=x+y
    finish=time.time
    distance=finish-start

    print(" Result {}. Function {} that time complated".format(result,distance))

Sum(2,4)

def Mulp(x,y):
    start=time.time()
    time.sleep(2)
    result=x*y
    finish=time.time
    distance=finish-start

    print(" Result {}. Function {} that time complated".format(result,distance))
Mulp(9,8)

import time
def timecounter(function):
    def wrapper(*args,**kwargs):
        start=time.time()
        time.sleep(2)
        function(*args,**kwargs)
        finish=time.time()
        diff=finish-start
        print(" This function took {} ".format(diff))
    return wrapper
@timecounter
def summ(x,y):
    result=x+y
    print(result)

@timecounter
def Mul(x,y):
    result=x*y
    print(result)

summ(2,4)

Mul(2,4)