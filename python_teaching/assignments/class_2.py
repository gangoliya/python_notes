# Create a class Rectangle that has attributes length and breadth, 
# and a method area() to calculate and return the area of the rectangle. 
# Also, include a method perimeter() to return the perimeter. 
# Instantiate the class and print the area and perimeter for length = 5 and breadth = 3.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rect = Rectangle(5, 3)


print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
