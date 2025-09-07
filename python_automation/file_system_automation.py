# from pathlib import Path

# print(Path.cwd())

# # Current working dir
# # what are the contents in the folder
# # what are the types of files
# path = Path("python_automation\file_system_automation.py")

# print(path.parent)

# print(path.suffix)


# import os

# print(os.getcwd())
# print(os.listdir("."))
# os.mkdir("NewFolder")


# # shutil (high-level operations)

# import shutil

# shutil.copy("python_automation\example.txt", "jj/backup.txt")


# Current Working directory

from pathlib import Path
# print("Pathlib: ", Path.cwd())

import os
# print("os: ", os.getcwd())

# Create and list folders
folder = Path("python_automation/TestFolder")
folder.mkdir(exist_ok=True)
for item in folder.iterdir():
    print(item)


# # Create, rename and delete a file
# file = Path('python_automation/sample.txt') # path specified
# file.touch() # created a file
# file.rename("renamed.txt") # renamed the file


# Copy & Move (shutil)

import shutil
Path("copyme.txt").write_text("Hello")
shutil.copy("copyme.txt", "copyme_backup.txt")

shutil.move("copyme_backup.txt", "python_automation/TestFolder/copyme_backup.txt")
