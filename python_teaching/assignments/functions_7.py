# 2. Write a Python function that accepts only positional-only arguments 
#    for a person's first name and last name, and prints them.

def name(fst, lst, /):
    return fst + " " + lst

print(name("Rajesh", "Rukmani"))