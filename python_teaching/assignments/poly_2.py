# Create a base class Shape with a method draw(). 
# Derive two classes Circle and Rectangle that override draw() with different messages. 
# Create a list of shape objects and call draw() in a loop to demonstrate polymorphism.


class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

# List of shape objects
shapes = [Circle(), Rectangle(), Circle(), Shape()]

# Call draw() method on each shape
for shape in shapes:
    shape.draw()