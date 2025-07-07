# Syntax

# Opening the file

# open("path_to_file", "options")

# r - read - Default Option. Opens a file for reading, error if file does not exist
# a - append - Opens a file for appending, creates the file if it does not exist
# w - write - Opens a file for writing, creates the file if it doers not exist
# x - create - Creates the specified file, returns error if file exist

# How file is read option
# t - text - Default option
# b - binary - binary things

# f = open("file_1.txt")
# f = open("file_1.txt", "rt")


f = open("python_teaching/file_handling/file_1.jpg", "a+") # You have to use forward slash

print(f.readline(5))

f.close()