#encapsulation

#print(dir(str)) # 

class Employee:
    def __init__(self,Name,Salary,Age):
        self.Name=Name
        self.__Salary=Salary #encapsulation
        self.Age=Age
        self.__Raise=0.20

    def SalaeyRaise(self):
        self.__Salary=self.__Salary+self.__Raise*self.__Salary

    def getSalary(self):
        return self.__Salary
    
    def getRaise(self):
        return self.__Raise
    
    def setRaise(self,newrate):
        self.__Raise=newrate

Employee1=Employee("ktrn","sm",5500)

print(Employee1.Name)
print(Employee1.getSalary)
print(Employee1.getRaise)
Employee1.setRaise(0.50)