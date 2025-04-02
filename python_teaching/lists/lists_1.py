# Adding elements to the list

thislist = ['apple', 'cherry', 'banana']
# append() method

thislist.append('orange')
print(thislist)


# insert() method
thislist.insert(1, 'mango')
print(thislist)

# extend() method
thatlist = [1, 2, 3]
thislist.extend(thatlist)
print(thislist)

# + 
extended_list = thislist + thatlist
print(extended_list)

# Removing elements from the list

# remove() method
thislist = ['apple', 'cherry', 'banana']
thislist.remove("banana")
print(thislist)

# pop() method
thislist = ['apple', 'cherry', 'banana']
thislist.pop(1)
print(thislist)

# del() method
thislist = ['apple', 'cherry', 'banana']
del thislist[1]
print(thislist)

# clear() method
thislist = ['apple', 'cherry', 'banana']
thislist.clear()
print(thislist)

thislist = ['apple', 'cherry', 'banana']
newlist = []
for i in thislist:
    if 'c' in i:
        newlist.append(i)
print(newlist)

# Sorting the list

# sort() method - ascending order
thislist = ["banana",  "cherry", "apple"]
thislist.sort()
print(thislist)

thislist = [100, 53, 65, 23, 88]
thislist.sort()
print(thislist)

# sort() method - descending order
thislist = ["banana",  "cherry", "apple"] # apple, cherry, banana - reverse the index
thislist.sort(reverse = True) # ['cherry', 'banana', 'apple'] alphabetic
print(thislist)

thislist = [100, 53, 65, 23, 88]
thislist.sort(reverse = True)
print(thislist)

# reverse() method
thislist = ["banana",  "cherry", "apple", "mango"] # apple, cherry, banana - reverse the index
thislist.reverse() # [apple, cherry, banana] alphabetic
print(thislist)

# Copy the list
thislist = ['apple', 'cherry', 'banana']
thatlist = thislist

print(thatlist)

# copy() methods
thislist = ['apple', 'cherry', 'banana']
thatlist = thislist.copy()

thislist.append("orange")
thatlist.append("mango")

print(thatlist)