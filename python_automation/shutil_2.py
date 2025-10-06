# 3. Copying the content of one file to another
# 4. Replicating complete Directory
# 5. Removing a Directory
# 6. Finding files
# 7. Copying files from one os to another

# 3. Copying the content of one file to another

# .copyfile()


# import shutil

# source = r"C:\Users\gango\Documents\VS Code Files\python_notes\python_automation\test.py"

# destination =  r"C:\Users\gango\Documents\VS Code Files\python_notes\python_automation\TestFolder_2\test.py"

# dest = shutil.copyfile(source, destination)

# print("Destination path: ", dest)


# 4. Replicating complete Directory
# .copytree()
# shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, ignore_dangling_symlinks = False)
# import os, shutil

# path = os.getcwd() + "/python_automation"
# print(path)

# print("Before copying files: ")
# print(os.listdir(path))

# src = path + "/TestFolder_2"
# print(src)

# destination = path + "/TestFolder_3"
# print(destination)

# dest = shutil.copytree(src, destination)

# print("After copying files: ")
# print(os.listdir(path))


# copy - rglob() .txt, .pdf


# 5. Removing a Directory
# .rmtree()
# Syntax: shutil.rmtree(path, ignore_errors=False, onerror=None)

# import os, shutil

# location = os.getcwd()

# dir = "TestFolder_3"

# path = os.path.join(location, dir)
# print(path)


# shutil.rmtree(path)

# Acces Denied - VS Code

# 6. Finding files
# shutil.which()
#  shutil.which(cmd, mode = os.F_OK | os.X_OK, path = None)



# import shutil

# cmd = "shutil_1"

# locate = shutil.which(cmd)

# print(locate)


# 7. Copying files from one os to another


# one computer with multiple storages
# windows storage
# wsl - fedora
import shutil

src = r"C:\Users\gango\Documents\VS Code Files\python_notes\python_automation\test.py"

dest = r"\\wsl.localhost\FedoraLinux-42\home\gangoliya\Documents"

shutil.copy(src, dest)
print("File copied to Fedora from Windows")


# Storage - Mounted to both Linux and Windows - 