def average(*args):
    result=0
    for i in args:
        result=result+i
        result2 =result/len(args)
    return round(result2,3)

print(average(5,10,14,7))


def aver(*args,x):
    res=0
    for i in args:
        res=res+i
        res2=res/(len(args))
    if res2>x:
        print("{} is smaller than average".format(x))
    else:
        print("{} is bigger than average".format(x))

aver(5,7,8,100,15,14,x=15)


def cars(**kwargs):
    for key, value in kwargs.items():
        if value>250000:
            print("{} is little bir expensive".format(key))
        else:
            print("{} is not really expensive".format(key))

cars(Bwm=500000,Ausi=125000,mer=875000, Ford=150000)