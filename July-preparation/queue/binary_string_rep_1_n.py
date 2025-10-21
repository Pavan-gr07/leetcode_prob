# 1016. Binary String With Substrings Representing 1 To N

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "0110", n = 3
# Output: true
# Example 2:

# Input: s = "0110", n = 4
# Output: false
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 1 <= n <= 109



def binaryStringRepOneToN(s,n):
    
    for i in range(1,n+1):
        bin_val = bin(i)[2:]
        if bin_val not in s:
            return False
    return True


print(binaryStringRepOneToN("0110",4))