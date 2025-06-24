# r+ - read - Default Option. Opens a file for reading, erro if file does not exist
# a+ - append - Opens a file for appending, creates the file if it does not exist
# w+ - write - Opens a file for writing, creates the file if it doers not exist


with open("python_teaching/file_handling/example.txt", "r+") as f:
    print(f.read()) # Read the contents of the file
    # f.seek(0) # Move the pointer to beginning
    f.write("New Line")
    f.seek(0)
    print(f.read())
