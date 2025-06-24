# Syntax

# Opening the file

# open("path_to_file", "options")

# r - read - Default Option. Opens a file for reading, erro if file does not exist
# a - append - Opens a file for appending, creates the file if it does not exist
# w - write - Opens a file for writing, creates the file if it doers not exist
# x - create - Creates the specified file, returns error if file exist

# How file is read option
# t - text - Default option
# b - binary - binary things

# f = open("file_1.txt", "rt")
# f = open("file_1.txt", "rt")

# File Modes Beyond Basics

with open("python_teaching/file_handling/Day_29_Python_File_handling_Write_Create.pdf", "rb") as f:
    print(f.read(100))