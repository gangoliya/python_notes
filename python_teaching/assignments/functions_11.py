# 8. Write a Python function factorial that calculates the factorial of a given number using recursion.

def factorial(n):
    if n < 0:
        # return "Factorial is not defined for negative numbers"
        result =  "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        # return 1
        result =  1
    else:
        # return n * factorial(n - 1)
        result =  n * factorial(n - 1)

    return result
# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")
