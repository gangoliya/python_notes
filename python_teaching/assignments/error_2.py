# Create a function that takes a list of integers and returns the first even number. 
# Use exception handling to catch IndexError if no even number is found.

lst = [9, -1, -2, -4, 8]

try:
    for i in lst:
        if lst[i]%2 == 0:
            print(lst[i])
            break
except IndexError:
    print("No even number")
   