# File Pointer Manipulation

# file.seek(offset) - moves teh pointer
# file.tell() - returns the current position of the pointer

with open("python_teaching/file_handling/example.txt", "r+") as f:
    print(f.read())
    print(f.tell())
    f.seek(5)
    f.write("_")
    f.seek(0)
    print(f.read())