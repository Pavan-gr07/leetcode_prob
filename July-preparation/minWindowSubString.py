# 76. Minimum Window Substring

# avatar
# Discuss Approach
# arrow-up
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

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


# Counter usually store the frequency of the characters



from collections import Counter
def minWindowSubString(s,t):
    left,right =0,0
    target_count = Counter(t)
    min_len = float('inf')
    have = 0
    result =[-1, -1]
    need = len(target_count)
    window_count = {}

    while right < len(s):
       
        char = s[right]
        window_count[char] = window_count.get(char,0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            have += 1
        
        while have == need:

            if (right - left + 1) < min_len:
                min_len = right - left + 1
                result = [left, right]
            left_char = s[left]
            window_count[left_char] -= 1

            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                have -= 1

            left += 1

        right += 1
    


    return  s[result[0]:result[1]+1] if min_len != float('inf') else ""



x = 0
for i in range(1, 6):
    x = x + i*i
print(x)



print(minWindowSubString("ADOBECODEBANC","ABC"))