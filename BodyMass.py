print("Hi there Welcome to body mass calculation system")
Heigt=int(input("please input your length in cantimeters"))
Weight=int(input("Please give your weight"))

TheIndex= round(((Weight)/(Heigt/100)**2),2)

if TheIndex<=18.5:
    print("Your Index is {} You should gain weight".format(TheIndex))
elif TheIndex>18.5 and TheIndex<=24.9:
    print("Your Index is {} You are normal weight".format(TheIndex))
elif TheIndex>25 and TheIndex<=29.9:
    print("Your Index is {} You should loose weight".format(TheIndex))
elif TheIndex<40 and TheIndex<=30:
    print("Your Index is {} You should very loose weight".format(TheIndex))
elif TheIndex>40:
    print("Your Index is {} You should get medical asistance for weight".format(TheIndex))