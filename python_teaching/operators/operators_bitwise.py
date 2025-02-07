"""
Binary Numbers

0 - 0000 # 4 bit 0

1 - 0001

2 - 0010

3 - 0011

4 - 0100
0000000000000100
1111111111111100
-4

5 - 0101

6 - 0110

7 - 0111

8 - 1000

9 - 1001

10 - 1010

11 - 1011

12 - 1100


| Operator | Name | Description |
| --- | --- | --- |
| & | AND | Sets each bit to 1 if both bits are 1 |
| | | OR | Sets each bit to 1 if one of two bits is 1 |
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1 |
| ~ | NOT | Inverts all the bits |
| << | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| >> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |
"""

# & - and 
print(6 & 3)

# 0110
# 0011
# 0010


# | - or
print(6 | 3)

# 0110
# 0011
# 0111

# ^ XOR
print(6 ^ 3)

# 0110
# 0011
# 0101

# ~ NOT
print(~3)

# 0000000000000011
# 1111111111111100

# << - Left Shift - Multiply the number by 2
print(4<<1)

# 0100
# 10000

# >> - Right Shift - Divide the number by 4
print(4>>2)

# 0100
# 0010


