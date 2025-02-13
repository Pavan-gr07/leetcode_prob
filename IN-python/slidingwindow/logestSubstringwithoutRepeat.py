# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

def longestSubstring(str):
    ans,start,end=0,0,0
    freq ={}

    while end < len(str):
        freq[str[end]] = freq.get(str[end], 0) + 1 
        while freq[str[end]] > 1:
            freq[str[start]] -=1
            start +=1
        length = end-start+1
        if length > ans:
            ans = length

        end+=1

    return ans
def longest_unique_substring_length(s):
    start = 0
    ans = 0
    freq = {}
    
    for end in range(len(s)):
        if s[end] in freq:
            start = max(freq[s[end]], start)
        
        ans = max(ans, end - start + 1)
        freq[s[end]] = end + 1
    
    return ans



print(longest_unique_substring_length("pwwwkew"))
