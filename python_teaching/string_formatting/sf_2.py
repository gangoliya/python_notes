# .format() ->  before 3.6 top latest

# slower than f-string

price = 50
tax = 10
print("The price is {} dollars".format(price))

txt = "The price is {: .2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
price = 4
txt = "The quantity of the article is {} and price per article is {: .2f}."
print(txt.format(quantity, price))

# Index Numbers
quantity = 3
price = 4
txt = "The quantity of the article is {1} and price per article is {0: .2f}."
print(txt.format(quantity, price))

quantity = 3
price = 4
txt = "The quantity of the article is {1} and price {1} per article is {0: .2f}."
print(txt.format(quantity, price))

# Named Index
myOrder = "I have a {carname}, it is a {model}."
print(myOrder.format(carname = "Ford", model = "Mustang"))