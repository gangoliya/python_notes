from pathlib import Path

path = Path.cwd() /"shopping_list.md"
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))