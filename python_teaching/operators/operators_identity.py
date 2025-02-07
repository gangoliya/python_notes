x = [1, 2, 3]
y = [1, 2, 3]
z = x
# a: 1
# x, y, z have the same value ie. [1, 2, 3]

print(type(x))
print(type(y))

# is
print(x is z)

print(x is y)

print(x==y)


# is not
print(x is not z) # False

print(x is not y) # True

print(x!=y) # False
