# 4. Write a Python function that combines positional-only and keyword-only arguments
#    to print a person's first name (positional-only) and their city(keyword-only).

def details(fst_name, /, *, city):
    return fst_name + " lives in " + city

print(details("Ram", city="Delhi"))