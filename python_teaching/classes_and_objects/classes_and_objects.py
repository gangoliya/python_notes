# Python Classes
# Python Objects
# Python Properties
# Python Object Methods


# Synatc for creating a class

class MyClass:
    x = 5 # Property

# Creating an object
p1 = MyClass() # Object
print(p1.x)


# __init__() methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# __str__() methods
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})" # John(36)

p1 = Person("John", 36)

print(p1)


# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})" # John(36)
    
    def myFunc(self):
        print("Hello my name is " + self.name)
    
    def myDouble(self):
        return self.age * self.age
    
    

# Creating an Object
p1 = Person("John", 36)
p2 = Person("Rohit", 6)

# Calling the Object
print(p1)
p1.myFunc()
print(p1.myDouble())
print(p2.myDouble())



# self Parameter
class Person:
    def __init__(shabang, name, age):
        shabang.name = name
        shabang.age = age
    
    def __str__(shabang):
        return f"{shabang.name}({shabang.age})"
    
    def myFunc(shabang):
        print("Hello my name is " + shabang.name)


p1 = Person("John", 36)
print(p1)


# Modify Object Properties
p1.age = 40
print(p1.age)
p1.myFunc()

# Delete Object Properties
del p1.age
print(p1.name)

# Delete Objects 
# del p1
# print(p1)


# The pass statement
class Person:
    pass

class Person:
    def __init__(self):
        pass

p1 = Person()
print(p1)