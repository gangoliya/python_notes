"""
1. Ordered 
2. Unchangeable
3. Allow Duplicates
"""

thistuple = ("apple", "banana", "cherry") # [] - List () - tuple
print(thistuple)
print(type(thistuple))
# convert the tuple into a list and back to tuple
thattuple = ("apple", "mango", "cherry")
print(thattuple)

# length
print(len(thistuple))

# Creating tuple with only one element
thislist = ["apple"]
print(thislist)

thistuple = ("apple",) # to make a single element tuple we have to add comma
print(thistuple)
print(type(thistuple))

# Tuple Item - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40.0, "male")
print(tuple1)


# Access the elements in tuple - Ordered 
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])

# negative indexing
tuple1 = ("apple", "banana", "cherry")
#            -3        -2        -1
#              0        1           2
print(tuple1[-1])

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[2:])
# Slicing

print(tuple1[-4:-1])

print()
# Update Tuples

# Adding Elements
thistuple = ("apple", "banana", "cherry") 
print(thistuple)
print(type(thistuple))

thatlist = list(thistuple)
print(thatlist)
print(type(thatlist))

thatlist.append("mango")
thatlist.insert(1, "kiwi")
print(thatlist)
print(type(thatlist))


thistuple = tuple(thatlist)
print(thistuple)
print(type(thistuple))

print(thistuple)
print(type(thistuple))


print()
# Removing Elements
thistuple = ("apple", "banana", "cherry", "mango", "kiwi") 
print(thistuple)
print(type(thistuple))

thatlist = list(thistuple)
print(thatlist)
print(type(thatlist))

thatlist.remove("banana")
print(thatlist)
print(type(thatlist))

thatlist.pop(-1)
print(thatlist)
print(type(thatlist))

thistuple = tuple(thatlist)
print(thistuple)
print(type(thistuple))


# Sorting elements in Tuple - no sort method
# tuple1 = (3, 7, 98, 11, 90, 76)
# tuple1.sort()
# print(tuple1)


tuple1 = (3, 7, 98, 11, 90, 76, 3, 5, 55, 3)
print(tuple1)


a = (1, 2)
b = (3, 4)
c = a + b

print(c * 2) # c = c * 2


"""

key - value

a1: 'Apple'
b1: 'Mango'
"""