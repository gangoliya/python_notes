# def my_function(num): # param
#     print(num ** 2)

# my_function(2) # arguments
# my_function(4)
# my_function(6)
# my_function(8)


# Arguments

# def greetings(fname):
#     print(f"Hello {fname}!")

# greetings("Prashant")


def greetings(fname, lname = "Styles"):
    print(f"Hello {fname} {lname}!")

greetings("Harry")
greetings("Jerry")
greetings("Tom", "Singh")
greetings("Randhawa", "Raj")


# Keyword Arguments

greetings(lname = "Randhawa", fname = "Raj")
greetings(lname = "Singh", fname = "Tom")


# Arbitary Arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emily", "Harry", "Jerry", "Rohit")

# def my_function(num1, num2):
#     print(num1 + num2)

# def my_function(num): # param
#     print(num)



# my_function(5)
# my_function(5, 2)


# Return Statement

def squared_cubed(num, num1):
    num = num**2
    num1 = num1 ** 3
    return num, num1
    num = num ** 4
    pass


print(squared_cubed(2,2))


# The pass Statement
def my_func():
    pass

print(my_func())

