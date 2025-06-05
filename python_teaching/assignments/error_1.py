# Write a program that takes two numbers as input and divides the first number by the second. 
# Handle division by zero using try-except and print an appropriate message.

try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide number by zero.")