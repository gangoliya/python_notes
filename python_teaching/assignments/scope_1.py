# Global variable
count = 0

def increment():
    global count  # Declare that we are using the global variable
    print("Inside function, before increment:", count)
    count += 1
    print("Inside function, after increment:", count)

# Show value before calling the function
print("Before function call, count:", count)

# Call the function
increment()

# Show value after calling the function
print("After function call, count:", count)
