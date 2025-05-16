# Define a Python class called Person with attributes name and age. 
# Add a method greet() that prints a greeting message including the name and age. 
# Create an instance and call the greet() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")

name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
p1 = Person(name1, age1)
p1.greet()