# Write a function append_names(filename, names) that appends a list of names to the file, 
# each on a new line.

# Create function
def append_names(filename, names):
    with open(f"python_teaching/assignments/{filename}", "a") as f:
        for name in names:
            f.write(name + "\n")
    
    with open(f"python_teaching/assignments/{filename}", "r") as f:
        print(f.read())

# Calling function
name_list = ["Alice", "Bob", "Charlie"]
append_names("names.txt", name_list)