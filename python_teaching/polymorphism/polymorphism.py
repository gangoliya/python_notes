# Function/ Method Polymorphism

# len()

# String
x = "Hello World!"
print(len(x))

# Tuple
myTuple = ("apple", "cherry", "mango")
print(len(myTuple))

# Dictionary

myDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(myDict))



# Class Polymorphism


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# car1.move()
# boat1.move()
# plane1.move()

for x in (car1, boat1, plane1):
    x.move()


# Inheritance Class Polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()


make_sound(Cat())
make_sound(Dog())