# Create a program that writes the text "Start of log" to log.txt using "w" mode, 
# then appends "Log updated" using "a" mode. 
# Print the contents of the file.

# Write "Start of log" to log.txt using "w" mode
with open("python_teaching/assignments/log.txt", "w") as file:
    file.write("Start of log\n")

# Append "Log updated" to log.txt using "a" mode
with open("python_teaching/assignments/log.txt", "a") as file:
    file.write("Log updated\n")

# Read and print the contents of the file
with open("python_teaching/assignments/log.txt", "r") as file:
    print(file.read())
