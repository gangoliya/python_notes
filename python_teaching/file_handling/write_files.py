with open("python_teaching/file_handling/file_2.txt", "w") as f:
    f.write("This is a new file.")

with open("python_teaching/file_handling/file_2.txt", "r") as f:
    print(f.read())