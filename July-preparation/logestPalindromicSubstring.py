# 5. Longest Palindromic Substring

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 


# def longestPalindrome(s):
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]
#     start = 0
#     max_len = 1

#     # All substrings of length 1 are palindromes
#     for i in range(n):
#         dp[i][i] = True

#     # Check for substring of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             start = i
#             max_len = 2

#     # Check lengths greater than 2
#     for length in range(3, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1

#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 if length > max_len:
#                     start = i
#                     max_len = length

#     return s[start:start + max_len]


def palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def longestPalindrome(s):
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # when while ends, left and right moved 1 step extra
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Odd length palindrome
        l1, r1 = expand(i, i)
        if r1 - l1 + 1 > max_len:
            start = l1
            max_len = r1 - l1 + 1
        
        # Even length palindrome
        l2, r2 = expand(i, i + 1)
        if r2 - l2 + 1 > max_len:
            start = l2
            max_len = r2 - l2 + 1
    
    return s[start:start + max_len]

print(longestPalindrome("baba"))
