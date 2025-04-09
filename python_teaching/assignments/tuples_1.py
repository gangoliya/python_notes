# 3. Write a Python function that accepts a tuple of numbers and returns the maximum value.

tuple1 = (1, 99, 599, 899, 34, 8909, 45)

def func_max(nums: tuple[int]):
    maximum = max(nums)
    return maximum

print(func_max(tuple1))