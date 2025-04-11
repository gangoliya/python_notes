"""
- There are 4 built-in data types in Python used to store collections of data:
    1. List 
    2. Tuple
    3. Set
    4. Dictionary
    tuple(), list()
"""

# a =  [1, 2]
# c, d = a

# print(c)
# print(d)

# Sets

thisset = {1, 2, 3}

# Specifications of sets
# 1. Unordered
# 2. Unindexed
# 3. Unchangable (Exception: You can add or remove values)
# 4. Do no allow duplicates

# 1. Unordered
thisset = {"apple", "mango", "cherry"}
print(thisset)
print(thisset)

thisset = {1, 2, 3}
print(thisset)
print(thisset)

# 2. Unindexed
# thisset = {"apple", "mango", "cherry"}
# print(thisset[1])

# 4. Do no allow duplicates
thistuple = ("apple", "banana", "cherry", "apple")
thisset = set(thistuple)
print(thisset)

thisset = {"apple", "banana", "cherry", "apple", True, 1, 2}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple", False, 0, 2}
print(thisset)


# Set Methods
# Length

thisset = {"apple", "banana", "cherry", "apple", True, 1, 2}
print(len(thisset))

# set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
print(type(thisset))


# Access the elements in python
thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#     if x == "apple":
#         thisset[x] = "orange"

# 3. Unchangable

# Add elements to set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thatset = {"orange", "kiwi"}

thisset.update(thatset)

print(thisset)

# Remove elements from set
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("kiwi")
# print(thisset)

# discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("kiwi")
print(thisset)

# pop
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

# clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)


thisset = {"apple", "banana", "cherry"}
thislist = list(thisset)
print(thislist)
print(type(thislist))