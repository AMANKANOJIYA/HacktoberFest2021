# this program is just an example of to do single level inheritance in python


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_hoildays=21
    def __init__(self, aname, asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages=languages



    def printprog(self):
        return f"The Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role} the languages are {self.languages}"

    
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
shub = Programmer("shub",555,"Programme",["python","cpp"])
karan = Programmer("karan",750,"Programme",["java"])

print(karan.printprog())
print(shub.printprog())
print(karan.printdetails())
print(karan.no_of_hoildays)

