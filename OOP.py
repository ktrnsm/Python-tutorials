#object oriented programming

x="hiThere"
print(type(x))
print(x.index("T")) # indeksleme aranan karakterin kaçıncı karakter olduğunu beliertiyor.
y="ktrn"
print(y.index("r"))


class Human:
    pass # hatasız çalışması için pass kullanıyor

z=Human()
print(type(z))

class Humani():
    Name="ktrn"
    LName="sm"
    Age="22"
    HairColor="Blue"

print(Humani.Name)
print(Humani.HairColor)

class Hombre: # sınıf oluştururken def init olmak zorunda
    def __init__(self,Name,Lame,Age,HairColor):
        self.Name=Name
        self.Lame=Lame
        self.Age=Age
        self.HairColor=HairColor
Hombre1=Hombre("ktrn","sm","22","blue")
Hombre2=Hombre("sm","ktrn","37","Brown")

print(Hombre1.Name)
print(Hombre2.Name)
        
