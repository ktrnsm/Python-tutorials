class Human():
    def __init__(self,Name,LastName,Haircolor,Height,Weight):
        self.Name=Name
        self.LastName=LastName
        self.Haircolor=Haircolor
        self.Height=Height
        self.Weight=Weight

class Student(Human):
    def __init__(self, Name, LastName, Haircolor, Height, Weight,School,Age):
        super().__init__(Name, LastName, Haircolor, Height, Weight)
        self.School=School
        self.Age=Age

Humana=Human("ktrn","sm","blue",195,89)
Studenta=Student("sm","ktrn","black",188,99,"Math",24)

print(Humana.Haircolor)
print(Studenta.School)