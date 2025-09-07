# # from pathlib import Path

# # p = Path('.')
# # [x for x in p.iterdir() if x.is_dir()]


# # open()

# # 'C:\Users\gango\Documents'
# # Traditional Way
# import glob # identifying the type of files
# import os # traversing through your file systems
# import shutil # moving the file

# for file_name in glob.glob("*.txt"):
#     new_path = os.path.join("archive", file_name)
#     shutil.move(file_name, new_path)


# # storage -> abc.txt
# # archive -> abc.txt


# # pathlib

# from pathlib import Path

# for file_path in Path.cwd().glob("*.txt"):
#     new_path = Path("archive") / file_path.name
#     # new_path2 = Path.joinpath("archive", file_name)
#     file_path.replace(new_path)

# Path Installation with Pyhton's pathlib

# Path is the heart of pathlib

# from pathlib import Path

# # Path.cwd()

# # Passing in a String

# print(Path(r"C:\Program_Files\realpython\file.py"))


# # Joining Paths

# new_path = Path("archive") / file_path.name
# new_path2 = Path.joinpath("archive", file_name)


# from pathlib import Path

# for file_path in Path.cwd().glob("*.txt"):
#     new_path = Path("archive") / file_path.name
#     file_path.rename(new_path)


# Reading & Writing Files

from pathlib import Path


path = Path.cwd() /"shopping_list.md"
with path.open(mode = 'r', encoding="utf-8") as md_file:
    content = md_file.read() # single line read ["#ShoppingList", "##Fruit", "*Banana", *Apple *Peach * Chocolate *Bits"]
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))


# for line in content.splitlines():
#     if line.startswith("*")

#Banana *Apple *Peach * Chocolate *Bits
