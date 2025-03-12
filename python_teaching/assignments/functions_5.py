# 9. Reverse a string

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

str = input("Enter string to reverse: ")
print(reverse_string(str))