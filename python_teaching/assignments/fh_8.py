# Write a context manager class that tracks when the file was opened and closed

import datetime

class FileTracker:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.opened_at = None
        self.closed_at = None

    def __enter__(self):
        self.opened_at = datetime.datetime.now()
        print(f"[Opened] {self.filename} at {self.opened_at}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed_at = datetime.datetime.now()
        self.file.close()
        print(f"[Closed] {self.filename} at {self.closed_at}")

with FileTracker("sample.txt", "w") as f:
    f.write("Tracking file open and close time.")