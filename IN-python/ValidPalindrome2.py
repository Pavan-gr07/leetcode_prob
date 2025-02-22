# 680. Valid Palindrome II
# Easy
# Topics
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

def validPalindrome2(s):
    for i in range(len(s)):
        temp = s[:i]+s[i+1:]
        
        if( temp == temp[::-1]):
            return True
    return False


def validPalindrome2a(s):
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character and check for palindrome
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True 
print(validPalindrome2a("abca"))