# The `__enter__` method is called when you enter the with block, and its return value is assigned to a variable within that block.
# The `__exit__` method, on the other hand, is called when the `with` block exits, regardless of whether it finishes normally or with an exception.

import datetime

class SimpleLogger:
    def __init__(self, filename, mode='a'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

log_file_name = "python_teaching/file_handling/example_1.txt"

with SimpleLogger(log_file_name, "a") as f:
    try:
        f.write(f"[{datetime.datetime.now()}] INFO: Custom log entry. \n")
    except: 
        f.write(f"[{datetime.datetime.now()}] INFO: Custom log file created. \n")

with SimpleLogger(log_file_name, "a+") as f:
    f.write(f"[{datetime.datetime.now()}] INFO: Another log entry. \n")


with open(log_file_name, 'r') as f:
    print(f.read())



#   [2023-10-27 10:00:01] INFO: File 'example.txt' logged in.
#   [2023-10-27 10:00:05] WARN: Failed login attempt for 'Bob'.
#   [2023-10-27 10:00:10] INFO: Service 'payments' started.