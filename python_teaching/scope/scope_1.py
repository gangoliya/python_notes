# Scope

# # Local Scope
# def myFunc():
#     x = 300
#     print(x)

# myFunc()
# # print(x)


# # Function Inside Function
# def myFunc():
#     x = 300
#     print(x)
#     def myInnerFunc():
#         print(x)
#     myInnerFunc()

# myFunc()
# # myInnerFunc()


# Global Scope

# x = 300

# def myFunc():
#     print(x)

# myFunc()
# print(x)


# Naming Variables

# x = 300

# def myFunc():
#     x = 200
#     print(x)

# myFunc()
# print(x)

# Global Keyword
def myFunc():
    global x
    x = 300
    print(x)

myFunc()
print(x)

x = 3000

def myFunc():
    global x
    x = 200
    print(x)

myFunc()
print(x)

# Nonlocal Keyword
def myFunc1():
    x = "Rohit"
    def myFunc2():
        nonlocal x
        x = "Hello"
        print(x)
    myFunc2()
    return x

print(myFunc1())
print(x)