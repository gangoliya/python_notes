# Robust Exception Handling for File Operations

# try:
#     with open("missing.txt", "r") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("File not found!")

import time

for i in range(3):
    try:
        with open("data.txt") as f:
            break
    except FileNotFoundError:
        time.sleep(2)