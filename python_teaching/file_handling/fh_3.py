with open("python_teaching/file_handling/example.txt", "a+") as f:
    f.write("\nAppend Line")
    f.seek(0) # Move the pointer to beginning
    print(f.read())