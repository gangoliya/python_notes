import os


# - Handling the Current Working Directory
# 1.1 Getting CWD
# print(os.getcwd())

# 1.2 Changing the directory
# def current_path():
#     print("Current working Directory: ")
#     print(os.getcwd())
#     print() # getting a new line

# current_path()
# os.chdir(r'C:\Users\gango\Documents\VS_Code_Files\python_notes\python_teaching\assignments')
# current_path()


# - Creating a Directory

# - os.mkdir()
# - os.makedirs()

# directory = 'c'
# parent_dir = r'C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\Rohit'

# path = os.path.join(parent_dir, directory) # creating string for the folder
# os.makedirs(path) # creating the folder
# print("directory '%s' created" % directory)


# parent_dir = r'C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\Rohit\a\b'
# path = os.path.join(parent_dir, directory) # creating string for the folder
# os.makedirs(path) # creating the folder
# print("directory '%s' created" % directory)
# directory = "Prashant"

# mode = 0o666 # octal format - read & write permission for the owner

# path = os.path.join(parent_dir, directory) 
# os.mkdir(path)

# print("directory '%s' created" % directory)





# - Listing out Files and Directories with Python

# path = "/" # home - c folder
# dir_list = os.listdir()

# # print("Files and directories in '" "': ")
# print(dir_list)


# - Deleting Directory or Files using Python
# os.remove() - files
# os.rmdir() - directories

# file = 'c'
# location = r'C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\Rohit\a\b'


# os.chmod(r"C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\Rohit\a\b\c", 0o600)

# path = os.path.join(location, file)
# os.rmdir(path)

# - File Permissions and Metadata
# chmod
# os.chmod(r"C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\Rohit\a\b\c", 0o600)
# chown
# os.chown("path", 1000, 1000)

# os.stat()

path = r"C:\Users\gango\Documents\VS_Code_Files\python_notes\python_automation\new_1.md"
stats = os.stat(path)

print(os.path.basename(path))
print("Size: ", stats.st_size, "bytes")
print("Last modified: ", stats.st_mtime)
print("Permissions: ", oct(stats.st_mode)[-3:])


# Additional Functions
