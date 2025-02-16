# Write a Python program that uses a while loop to calculate the sum of numbers from 1 to 50.

i = 1
s = 0

while i <=50:
    s += i
    i += 1

print(f"Sum of first {i-1} integers is {s}")