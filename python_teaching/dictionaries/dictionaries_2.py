# Removing Items
# pop() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")
print(thisdict)

# popitem() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()
thisdict.popitem()
print(thisdict)

# del keyword
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict["brand"]
print(thisdict)

# del thisdict
# print(thisdict)


# clear() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)


# Loop Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for i in thisdict:
    print(i)

for i in thisdict.keys():
    print(i)


for i in thisdict:
    print(thisdict[i])

for i in thisdict.values():
    print(i)

for x, y in thisdict.items():
    print(x, ":", y)

# Copy Dictionaries
# copy() method
# thatdict = thisdict (reference)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thatdict = thisdict.copy()
print(thatdict)


# dict()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thatdict = dict(thisdict)
print(thatdict)


# Nested Dictionaries
mychild = {
    "child1": {
        "name": "Toby",
        "year": 2004
    },
    "child2": {
        "name": "Emily",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# another way
child1 = {
        "name": "Toby",
        "year": 2004
    }

child2 = {
        "name": "Emily",
        "year": 2007
    }

child3 = {
        "name": "Linus",
        "year": 2011
    }

mychild = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}


print(mychild)
print(mychild['child2']["name"])

print("--------------------------")

for x, obj in mychild.items():
    print(x) # x = child1, obj = {name: Toby, year: 2004}

    for y in obj:
        print(y + ":" , obj[y]) # name: Toby, year: 2004

print("--------------------------")


# Lambda Function
# Syntax
# lambda arguments: expression
# lambda a: a * a

x = lambda a: a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.

def myfunc(n):
    return lambda a : a * n # n = 2, a = 11; # n = 3, a = 11
    # def my_func2(a):
    #   return a * n


mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))