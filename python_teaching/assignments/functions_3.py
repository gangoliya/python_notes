# Calculate the area of rectangle

def area(len, wid):
    ar = len * wid
    return ar

len = int(input("Enter length: "))
wid = int(input("Enter width: "))
print(area(len, wid))