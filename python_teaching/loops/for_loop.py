""" 
There are 3 types of loops in Python:

- For
- While
- Nested (Loop inside a loop)

"""

fruits = ["apple", "banana", "cherry"]

# for i in fruits:
#     print(i)
#     print('----')


# fruits[0]
# fruits[1]
# fruits[2]

# fruit = 'banana' # b a n a n a # 1024 1025 1026
# print(fruit[0])
# for i in fruit:
#     print(i)


# for i in range(10, 5, -1):
#     print(i)

# print("Finally Finished!")

# range(2, 6) # 
# range(2, 10, 2)


# break -- coming out of the loop


# for i in fruits:
#     print(i)

#     if i == "banana":
#         break

#     print(i)

# print("Loop Finished!")


# continue - continues the loop skipping the current loop


fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)

    if i == "banana":
        continue

    print(i)


print("Loop Finished!")


for i in range (1, 101):
    if i == 99:
        break
    print(i)


