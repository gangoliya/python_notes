# Write two classes Bird and Fish, each with a method move() that prints "Fly in the sky" and "Swim in the water" respectively. 
# Write a function describe_movement() that takes an object and calls its move() method to demonstrate polymorphism.

class Bird:
    def move(self):
        print("Fly in the sky")

class Fish:
    def move(self):
        print("Swim in the water")

def describe_movement(creature):
    creature.move()

# Example usage:
bird = Bird()
fish = Fish()

describe_movement(bird)  # Output: Fly in the sky
describe_movement(fish)  # Output: Swim in the water
