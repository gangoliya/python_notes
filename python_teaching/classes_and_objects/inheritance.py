# Python Class Inheritance
# OOPS - Object Oriented Programming; Inheritance, Abstraction, Encapsulation, Polymorphism

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        # self.firstname = firstname
        # self.lastname = lastname
        self.graduationyear = year

    def printn(self):
        print(f"Hello! my name is {self.firstname} {self.lastname} and I graduated in {self.graduationyear}")

    

    

y = Person("John", "Doe")
y.printname()

x = Student("Mike", "Jordan", "2019")
x.printname()
x.printn()