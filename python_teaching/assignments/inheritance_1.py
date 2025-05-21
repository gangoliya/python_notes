# Create a base class  Vehicle  with a method  start_engine()  that prints "Engine started". 
# Derive a class  Car  from it that adds a method  play_music()  which prints "Playing music". 
# Create an object of  Car  and call both methods.

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def play_music(self):
        print("Playing music")

car1 = Car()
car1.start_engine()
car1.play_music()

# self is required in instance methods to access instance attributes and methods.