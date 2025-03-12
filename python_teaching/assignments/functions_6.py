"""
1. Implement a Python function using method overloading (using default arguments) to 
    calculate the area of a square and a rectangle. 
    - If only one argument is given, calculate the area of a square. 
    - If two arguments are given, calculate the area of a rectangle.
"""

def area(len, wid = None):
    if wid is None:
        return len ** 2
    else:
        return len * wid

print(area(5, 6))    