try:
    # Attempt to open and read from a file
    file = open("sample.txt", "r")
    content = file.read()
    print("File contents:\n", content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    # Ensure the file is closed if it was successfully opened
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
