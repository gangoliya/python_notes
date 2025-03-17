# 7. Factorial of a number

def fact(num): # 5
    result = 1
    for i in range(1, num+1): # 1, 6 (1 - 5)
        result *= i # fct = fct * i
    return result


number = int(input("Enter number for factorial: "))
print(fact(number))