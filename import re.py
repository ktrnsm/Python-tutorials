import re

x="hi there, my name is red"

y=re.findall("e",x)
print(y)

z=re.split(" ",x)
print(z)

t=re.sub("e","*",x)
print(t)

k=re.search("hi",x)
print(k.span()) # nesne içerisindeki kaçıncı kadarkterler arası olduğunu gösterir.
print(k.end())
print(k.string)

l=re.findall("[a-z]",x)
print(l)
m=re.findall("^[a-f]",x) # aralık haricinde arar

i=re.findall("i$",x) #en son karakteri soruyoruz.
j=re.findall("...",x) # 3 hadt olarak döndürür


birthdate="1998"
letters=["\?","\,","\+"]

def passcontrol(password):
    if len(password)<8:
        raise Exception("min 8 letters please")
    elif not re.search("[a-z]",password):
        raise Exception("min 1 small letter")
    elif not re.search("[A-Z]",password):
        raise Exception("min 1 Big letter")
    elif not re.search("[0-9]",password):
        raise Exception("min 1 number")
    elif not re.search(letters,password):
        raise Exception(" need and exteme letter")
    elif password.startswith(birthdate):
        raise Exception(" cannot start with Birthday")
    elif password.endswith(birthdate):
        raise Exception("cannot end with birthday")
    
    else:
        print("succesfullu created")

while True:
    try:
        password:input("please create the passworld")
        passcontrol(password)
    except Exception as ex:
        print(ex)
    else:
        break