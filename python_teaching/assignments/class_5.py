# Demonstrate the concept of class inheritance by creating a class Animal with a method speak() 
# and another class Dog that inherits from Animal and overrides the speak() method to say "Bark".

# Base class
class Animal:
    def speak(self):
        return "Some generic animal sound"

# Derived class
class Dog(Animal):
    def speak(self):
        return "Bark"

# Create objects
animal = Animal()
dog = Dog()

# Call speak method
print("Animal says:", animal.speak())
print("Dog says:", dog.speak())
