# Path handling with os and pathlib

import os

folder = "python_teaching/file_handling/"
path = os.path.join(folder, "file.txt")


# pathlib
from pathlib import Path

file = Path(folder)/ "file.txt"
print(file.exists())


# python code - interpreter - machine(cpu)