# Demonstrate the use of  finally block by writing a program that opens a file, 
# reads its contents, and ensures the file is closed even if an exception 
# occurs.

try:
    file = open("python_teaching/error_handling/exist.txt", "r") # opening the file
    content = file.read() # reading the file
    print("File contents :", content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print("An unexpected error has occured: ", e)

finally:
    try:
        file.close()
        print("File is closed successfully")
    except NameError:
        print("File was never opened, so nothing to close.")