"""
There are total of 4 array structures or as we call them collections of data:
    1. Lists []
    2. Tuples ()
    3. Set
    4. Dictionary - key value pair {}

"""

lst = ['apple', 'cherry', 'banana', 'banana']

lst2 = ['mango']

lst2.append(lst)
# ['mango', ['apple', 'cherry', 'banana', 'banana']]

print(lst2[1][:3])

# print(type(lst2[0]))

# # len() function - return the length of the list

# print(len(lst)) # 4
# print(len(lst2)) # 2

# nums = [1, 2, 3, 4]

# for i in range(len(nums)): # range(0, 4)
#     print(nums[i])

list1 = [1, 2, 3, 4]
list2 = ['apple', 'banana', 'cherry']
list3 = [True, False, 0, 1]

list4 = ['abc', 34, True, 2.5]


print(list1[:3])

# print(list4)
# print(type(list4))
# print(type(list4[0]))
# print(type(list4[1]))
# print(type(list4[2]))
# print(type(list4[3]))


# for i in range(len(list4)):
#     if isinstance(list4[i], int):
#         print(list4[i])

# for i in range(len(list4)):
#     if type(list4[i]) == 'bool':
#         print(list4[i])


# # list() constructor

# lst = list(('apple', 'cherry', 'banana'))
# lst[1] = 'mango'
# print(lst)
# print(type(lst))


