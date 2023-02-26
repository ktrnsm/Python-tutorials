x="Hi There"
print(x.index("T"))

class Human:
    def __init__(self,Name,LastName,BirthDay):
        self.Name=Name
        self.LastName=LastName
        self.Birthday=BirthDay
    def information(self):
        print("Hi There my name is {} and the Last name is {} and my Birthday is {}".format(self.Name,self.LastName,self.Birthday))
    def Age(self):
        return 2023-self.Birthday

#Sınıflar içierisinden nesne üretilir.

Humana=Human("ktrn","sm",2023)
Humanb=Human("sm","ktrn",1994)

Humana.information()
Humanb.information()

print(Humana.Age())
print(Humanb.Age())