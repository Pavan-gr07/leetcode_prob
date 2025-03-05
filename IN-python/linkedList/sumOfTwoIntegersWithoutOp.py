# 371. Sum of Two Integers
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
 

# Constraints:

# -1000 <= a, b <= 1000


# def sumOfOperators(a,b):
#     while b!=0:
#         carry = a & b
#         a = a ^ b
#         b = carry << 1
    
#     return a

def sumOfOperators(a, b):
    MAX = 0x7FFFFFFF  # Maximum positive int for 32-bit
    MASK = 0xFFFFFFFF  # Mask to keep numbers within 32-bit range

    while b != 0:
        carry = (a & b) & MASK  # Limit to 32 bits
        a = (a ^ b) & MASK  # Perform XOR within 32-bit range
        b = (carry << 1) & MASK  # Shift and mask

    # If a is a negative 32-bit number, convert it back to Python's signed int
    return a if a <= MAX else ~(a ^ MASK)

# Test cases
print(sumOfOperators(2, 2))   # Output: 4
print(sumOfOperators(1, -1))  # Output: 0 ✅ No infinite loop

def sumOfOperators(a,b):
    
    return sum([a,b])

print(sumOfOperators(2,2))