# Create a Python script that checks if notes.txt exists. 
# If it doesn't, create it using "x" mode. 
# If it does, append "Checked on " using "a" mode. Use the datetime module.

from datetime import datetime

fname = "python_teaching/assignments/notes.txt"

try:
    # Try creating the file with "x" mode
    with open(fname, "x") as f:
        f.write("File created on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    
    # Read the file
    with open(fname, "r") as f:
        print(f.read())

except FileExistsError:
    # If file already exists, append the check timestamp
    with open(fname, "a") as f:
        f.write("Checked on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    
    # Read the file
    with open(fname, "r") as f:
        print(f.read())
