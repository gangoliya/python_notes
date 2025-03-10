# Check whether the number is even or not - Return True or False

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter number to chcek for even: "))
print(even(number))