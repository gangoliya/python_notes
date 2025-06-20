# Syntax

# Opening the file

# open("path_to_file", "options")

# r - read - Default Option. Opens a file for reading, erro if file does not exist
# a - append - Opens a file for appending, creates the file if it does not exist
# w - write - Opens a file for writing, creates the file if it does not exist
# x - create - Creates the specified file, returns error if file exist

# How file is read option
# t - text - Default option
# b - binary - binary things

# f = open("file_1.txt")
# f = open("file_1.txt", "a")

with open("python_teaching/file_handling/file_2.txt", "a") as f:
    f.write("\nThis is a new file.")

with open("python_teaching/file_handling/file_2.txt", "r") as f:
    print(f.read())