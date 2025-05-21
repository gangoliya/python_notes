# Create a base class  Shape  with a method  area() . Create two derived classes 
# Circle  and  Square  that override the  area()  method to calculate area 
# appropriately. Instantiate both and display their areas.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self, n, m):
        return 3.14 * n * n
    
class Square(Shape):
    def area(self, n):
        return n * n
    
c1 = Circle()
s1 = Square()

print(c1.area(5))
print(s1.area(5))