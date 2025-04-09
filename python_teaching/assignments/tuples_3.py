# 6. Create a tuple of 5 integers and write a program to reverse the tuple 
#       without using built-in reversed() function or slicing.

tuple1 = (1, 99, 599, 899, 34)

n = len(tuple1)
list1 = []
while n>0:
    list1.append(tuple1[n-1])
    n -= 1

tuple1 = tuple(list1)
print(tuple1)