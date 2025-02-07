# input()

# val = float(input("Enter a value: ")) # str

a = 100
b = 50
c = 200

# AND 
if a>b and c>a and b<c:
    print("conditions are True")
else:
    print("One or more conditions is False")


# OR
if a>b or a>c:
    print("One or more conditions are True")
else:
    print("Both the conditions are False")

# NOT

if not(a<b):
    print("a is greater than b")


if a>b and not(c<b):
    print("True")
else:
    print("False")
