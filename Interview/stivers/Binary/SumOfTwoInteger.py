# 371. Sum of Two Integers
# Solved
# Medium
# Topics
# Companies
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5



def SumOfInteger(a,b):
    while b != 0:
        carry = a & b       # common set bits of a and b
        a = a ^ b           # sum of bits where at least one is not set
        b = carry << 1      # carry is added to the next bit
    return a



def SumOfInteger1(a,b):
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        carry = (a & b) & MASK
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK

    return a if a <= MAX_INT else ~(a ^ MASK)



print(SumOfInteger1(3,2))