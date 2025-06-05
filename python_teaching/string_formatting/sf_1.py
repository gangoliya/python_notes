# f-string
dollars = 50
txt = f"This price is {dollars} dollars" # placeholder
print(txt)

# Modifier
price = 60.98765
txt = f"This price is {price: .2f} dollars"
print(txt)

# Perform operations
qty = 5
price = 10
txt = f"This total is {price * qty: .2f} dollars"
print(txt)

# if...else conditional formatting
price = 51
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# execute functions
fruit = "apple"
txt = f"I love {fruit.upper()}"
print(txt)


def my_conv(x):
    return x * 0.3048 # feet to meters

txt = f"The plane is flying at a {my_conv(3000): .2f} meter altitude."
print(txt)



dollars = 500000
txt = f"This price is{dollars: ,} dollars" # placeholder
print(txt)


# format
# txt = "The price {} dollars".format(dollars, fin)