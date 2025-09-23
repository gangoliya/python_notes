# Renaming Files
## .with_stem() - copying 
## .with_suffix() - .py, .md, .txt 
# from pathlib import Path

# txt_path = Path("C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/new_2.md")
# print(txt_path)


# md_path = txt_path.with_suffix(".pdf")
# print(md_path)

# txt_path.rename(md_path)
# print(txt_path)

## .with_name() - whole name as well as extension
# from pathlib import Path

# txt_path = Path("C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/example_1.txt")
# print(txt_path)


# md_path = txt_path.with_name("new_1.md")
# print(md_path)

# txt_path.replace(md_path)
# print(txt_path)


# Copying Files
# from pathlib import Path

# txt_path = Path("C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/new_1.md")
# print(txt_path)


# md_path = txt_path.with_name("new_2.md")
# print(md_path)

# md_path.write_bytes(txt_path.read_bytes())


# Moving & Deleting Files
# from pathlib import Path

# txt_path = Path("C:/Users/gango/Documents/VS Code Files/python_notes/python_automation/new_1.md")
# print(txt_path)

# new_path = Path("C:/Users/gango/Documents/VS Code Files/python_notes/new_1.md")

# txt_path.replace(new_path)

# Deleting notes to be added

# Creating Empty Files
# .touch()
# from pathlib import Path

# filename = Path("hello.txt")

# print(filename.exists())

# filename.touch(exist_ok=False) # created this files
# print(filename.exists())

# pathlib examples

## Counting Files

# from pathlib import Path

# from collections import Counter


# print(Counter(path.suffix for path in Path.cwd().iterdir()))


# # Counter({'': 6, '.txt': 3, '.py': 1, '.md': 1})

## Displaying a Directory Tree

# from pathlib import Path

# def tree(directory):
#     print(f"{directory}")
#     for path in sorted(directory.rglob("*")):
#         depth = len(path.relative_to(directory).parts)
#         spacer = "    " * depth
#         print(f"{spacer}+ {path.name}")


# tree(Path.cwd())