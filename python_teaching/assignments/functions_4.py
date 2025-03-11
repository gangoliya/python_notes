# Factorial of a number

def fact(num):
    fct = 0
    for i in range(1, num+1):
        fct *= i
    return sum


number = int(input("Enter number for factorial: "))
print(fact(number))