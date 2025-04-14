# Sets Method

"""
Join Sets
- union() and update() join 2 sets, but no duplicates taken
- intersection() print the common values
- difference() method keeps the items that are not in the other set
-  symmetric_difference() method keeps all the items EXCEPT the duplicates

"""


# Union() / (|)
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# set3 = set1 | set2
# print(set3)

# set3 = {"Rohit", "Prashant"}

# set4 = set1.union(set2, set3)
# print(set4)

# set4 = set1 | set2 | set3
# print(set4)


# # Join a set & tuple

# thisset =  {"a", "b", "c"}
# thistuple = (1, 2, 3)

# set_1 = thisset.union(thistuple)
# print(set_1)
# print(type(set_1))


# Update()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3, "c"}

# set1.update(set2)
# print(set1)

# set3 = set1.union(set2)
# print(set3)

# Intersection (&)

# set1 = {"apple", "banana", "orange"}
# set2 = {"apple", "google", "microsoft"}

# set3 = set1.intersection(set2)
# print(set3)

# set3 = set1 & set2
# print(set3)

# thisset =  {"a", "b", "c"}
# thistuple = (1, 2, 3, "c")

# set_1 = thisset.intersection(thistuple)
# print(set_1)
# print(type(set_1))


# thisset.intersection_update(thistuple)
# print(thisset)


# Difference (-)
# difference()
# difference_update()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.difference(set2)
# print(set3)

# set3 = set1 - set2
# print(set3)

# set1.difference_update(set2)
# print(set1)


# symmetric_diiference() / ^
# symmetric_difference_update()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "c"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3, "c"}
# set3 = set1 + set2
# print(set3)


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))