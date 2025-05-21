# Create a base class  Person  with attributes  name  and  age . 
# Derive a class Student  from  Person  and add  marks . 
# Include a method to display all information. 
# Create an object and demonstrate inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}. Marks: {self.marks}%")
    
s1 = Student("John Smith", 15, 85)
s1.display()