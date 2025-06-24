# Write a Python program to create a new file data.txt using "x" mode 
# and write the string "New file created." to it. 
# Handle the error if the file already exists.

try:
    with open("python_teaching/assignments/data.txt", "x") as f:
        f.write("New file created!")
    
    with open("python_teaching/assignments/data.txt", "r") as f:
        print(f.read())
except FileExistsError:
    print("File already exists!")