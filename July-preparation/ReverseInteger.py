# 7. Reverse Integer
# Attempted

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1



def reverseInteger(n):
    isNegative =  n < 0
    max_int = (1 << 31) - 1
    min_int = -(1 << 31)
    ans =0
    rev=0
    n = abs(n)
    while n != 0:
        rev = n % 10
        ans = ans * 10 + rev
        n = n // 10
    
    result = -ans if isNegative else ans
    if result > max_int or result < min_int:
        return 0
    
    return  result

print(reverseInteger(-123))

