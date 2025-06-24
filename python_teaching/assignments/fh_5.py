# Write a program to read a file input.txt, convert its contents to uppercase, 
# and write the results to output.txt using "w" mode.

# Read from input.txt
with open("python_teaching/assignments/input.txt", "r") as f:
    content = f.read()

# Convert to uppercase
uppercase_content = content.upper()

# Write to output.txt
with open("python_teaching/assignments/output.txt", "w") as f:
    f.write(uppercase_content)

# Read again
with open("python_teaching/assignments/output.txt", "r") as f:
    print("input:")
    print(f.read())

with open("python_teaching/assignments/output.txt", "r") as f:
    print("OUTPUT:")
    print(f.read())