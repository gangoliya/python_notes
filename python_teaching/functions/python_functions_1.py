# Method Overloading

# def my_func(num):
#     pass

# def my_func(num, num1 = 1):
#     pass


# Positional-Only Arguments

# def my_func(x, y, /):
#     return x
# print(my_func(4)) -- This will work
# print(my_func(x = 4)) -- This will give an error



# Keyword-Only Arguments

# def my_func(*, x):
#     return x

# print(my_func(x = 4)) # This will work
# print(my_func(4)) # This will give an error

# Combine Positional-Only and Keyword-Only Arguments
# def my_func(a, b, /, *, c, d):
#     return a, b, c, d

# print(my_func(3, 4, c = 5, d = 6))

# Recursion

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1) 
        # 6 + tri_recursion(5) # 6 +15 = 21
        # 5 + tri_recusrion(4) # 5 + 10 = 15
        # 4 + tri_recusrion(3) # 4 + 6 = 10
        # 3 + tri_recusrion(2) # 3 + 3 = 6
        # 2 + tri_recusrion(1) # 2 + 1 = 3
        # 1 + tri_recusrion(0) # 1 + 0 = 1
        print(result)
    else:
        result = 0

    return result

tri_recursion(6)


# factorial using normal loop
# factorial using recursion