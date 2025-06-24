# Custom Context Managers

# __enter__()
# __exit__()
import datetime

class MyFile:
    def __enter__(self):
        self.f = open("python_teaching/file_handling/example.txt", "w")
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
    