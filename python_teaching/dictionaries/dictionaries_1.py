"""
- There are 4 built-in data types in Python used to store collections of data:
    1. List 
    2. Tuple
    3. Set
    4. Dictionary --
"""

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)
print(type(thisdict))

# Access specific elements
print(thisdict["brand"])

# () - tuple
# [] - list
# {} - sets
# {key:value} - dict

# Ordered
print(thisdict)


# Changeable
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 1965
print(thisdict)


# Do not allow duplicate key
thisdict = { 
    "brand": "Ford",
    "brand2": "Ford",
    "model": "Mustang",
    "year": 1964
} 

print(thisdict)


# Methods of Dictionaries
# len() - length function
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))


thisdict = { 
    "brand": "Ford",
    "brand": "Honda",
    "model": "Mustang",
    "year": 1964
} 

print(len(thisdict))

# Data Items
thisdict = {
    "brand": "Ford", # String
    "electric": False, # Boolean
    "year": 1964, # Integer
    "colors": ["red", "blue", "white"] # List
}

# Use Case - Test Cases are defined
test1 = {
    "input": ["red", "blue", "white"],
    "output": 3
}

print(len(test1["input"]) == test1["output"])

# dict() constructor
thisdict = dict(name = "john", age = 36, country = "Norway")
print(thisdict)
print(type(thisdict))

# Acces Items in Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["brand"]
print(x)

# get()

x = thisdict.get("model")
print(x)

# keys() method
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "electric": False
}

x = car.keys()
print(x)

car["color"]= "Black"


x = car.keys()
print(x)


# values()

x = car.values()
print(x)

car["year"] = 2020
car["wheelSize"] = 16

x = car.values()
print(x)

# items()

x = car.items()
print(x)

# Exercise
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "brand" in thisdict:
    print("yes, it is present!")
else:
    print("no")

# Change Items in dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2018
print(thisdict)

# update()
thisdict.update({"year":2020})
print(thisdict)