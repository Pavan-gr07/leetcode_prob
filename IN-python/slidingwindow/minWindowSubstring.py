# 76. Minimum Window Substring
# Hard
# Topics
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

def minWindowSubString(s,t):
    i = 0
    j=len(t)
    curr_str = s[i:j]
    k=0
    while len(s):
        while k<len(t):
            if t[k]  in curr_str:
                k+=1
            else:
                if j < len(s):  # Ensure index doesn't go out of range
                    i += 1
                    j += 1
                    curr_str = s[i:j]
                    k = 0
                else:
                    break
        return curr_str
        
    return ""
# this will only captures 3 window 

from collections import Counter
def maintain_window(s, t):
    n = len(s)
    target_count = Counter(t)
    for size in range(len(t), n + 1):  # Start with len(t) and increase up to n
        i = 0
        while i + size <= n:  # Ensure window doesn't exceed string length
            curr_str = s[i:i + size]
            curr_count = Counter(curr_str)
            
            if all(curr_count[char] >= target_count[char] for char in target_count):  # Check if all chars of t are in curr_str
                return curr_str  # Return first valid substring
            i += 1  # Slide the window

    return ""  # Return empty if no valid substring found



# TC O(N^2)


# from collections import Counter

# def min_window(s, t):
#     if not t or not s:
#         return ""
    
#     target_count = Counter(t)  # Frequency count of t
#     window_count = Counter()
    
#     left = 0  # Left pointer
#     min_len = float('inf')  # To store the minimum window length
#     min_window = ""  # To store the result
    
#     required = len(target_count)  # Number of unique chars needed
#     formed = 0  # Number of unique chars in the current window
    
#     for right in range(len(s)):  # Expand right pointer
#         char = s[right]
#         window_count[char] += 1
        
#         # If this character's count matches target_count, increase `formed`
#         if char in target_count and window_count[char] == target_count[char]:
#             formed += 1

#         # Try to shrink the window while it remains valid
#         while left <= right and formed == required:
#             if right - left + 1 < min_len:
#                 min_len = right - left + 1
#                 min_window = s[left:right + 1]

#             # Remove leftmost character and adjust counts
#             left_char = s[left]
#             window_count[left_char] -= 1
#             if left_char in target_count and window_count[left_char] < target_count[left_char]:
#                 formed -= 1  # One unique character is no longer satisfied
            
#             left += 1  # Move left pointer

#     return min_window

# # Test case
# s = "mjlrhtgtnqnlmoppurscuxfqhpqnhaqvjdotxummkbayprnkkfoeevwllmzuorryugttafgniilxzbjjgaplxlykxxemoymlefegmmtwuhttifeqftbeeapeztsqtgdxlhgzuzvogqkqxoheikjokysmtkenqhkdoqeksbbaslrrbawlkfavdsjwfnlxwydmqhxijaldlcuocsaoxalcuubzjmzfkcsblrlurwzeawseostoseqpbtqkgpssrmtddhzudbygxsknldbfkuulnlvvcpoubjzeqaawdacatmqgstlepipftmavcqrdcskuvkqynubgjrmbmzhchwhcijymcrsemcyhorfdlijubxxoxesgabjlmjzoarumvtvmmdpxlbunardzyvgywrlianzcgtrcmmqyphydisqlltkjqqkohvwjkvmrpdvdrlejsemdweohzyrprbdaybkjxycodxtukzdcdrhbvxjuyclrforfqdo"
# t = "pdsfgpadzagefa"
# print(min_window(s, t))


# TC - O(N)


print(maintain_window("bbaa","aba"))