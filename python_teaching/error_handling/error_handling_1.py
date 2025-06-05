# try
# except
# else
# finally


# try:
#     x = 300
#     print(x)
# except:
#     print("An error has occured!")

# Many exceptions
# try:
#     x = 5
#     print(x/0)
# except NameError:
#     print("Variable x is not defined")
# except:
#      print("Something else went wrong")



# else
# else runs if try runs
# try:
#     print(x)
# except:
#      print("Something else went wrong")
# else:
#      print("Code ran successfully")


# finally
# try:
#     print("Hello")
# except:
#      print("Something else went wrong")
# finally:
#      print("Part 1 ran successfully")

# try:
#     print(x)
# except:
#      x = "Something else went wrong"
# finally:
#      print("Part 2 ran successfully")

# Raise an error
# x = int(input("Enter the value: "))

# if x<0:
#     raise Exception("Sorry, no numbers below zero are allowed.")

# print(x)


x = "Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed!")
