# 1. Copying Files to another directory - file

# os
# shutil.copy(source, destination, *, follow_symlinks = True)

# import shutil

# source = r"C:\Users\gango\Documents\VS Code Files\python_notes\python_automation\test.py"
# destination = r"C:\Users\gango\Documents\VS Code Files\python_notes\python_automation\TestFolder\test.py"


# dest = shutil.copy(source, destination)

# print("Destination path:", dest)




# 2. Copying the Metadata along with File - file + metadata


# Python program to explain shutil.copy2() method 
    
# importing os module 
import os 

# importing shutil module 
import shutil 

# path 
path = 'C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/TestFolder'

# # List files and directories 
# # in '/home/User/Documents' 
# print("Before copying file:") 
print(os.listdir(path)) 


# Source path 
source = "C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/test.py"

# Print the metadeta 
# of source file 
metadata = os.stat(source) 
print("Metadata:", metadata, "\n") 

# Destination path 
destination = "C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/TestFolder/test_2.py"

# Copy the content of 
# source to destination 
dest = shutil.copy2(source, destination) 

# List files and directories 
# in "/home / User / Documents" 
print("After copying file:") 
print(os.listdir(path)) 

# Print the metadata 
# of the destination file 
metadata_2 = os.stat(destination) 
print("Metadata:", metadata_2) 

# Print path of newly 
# created file 
print("Destination path:", dest)


print("---------------test.py-------------------")
print("Metadata_test.py: ", os.stat("C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/TestFolder/test.py"))



# 3. Copying the content of one file to another
# 4. Replicating complete Directory
# 5. Removing a Directory
# 6. Finding files
# Copying files from one os to another