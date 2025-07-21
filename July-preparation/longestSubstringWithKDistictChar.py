# Longest Substring with K Uniques
# Difficulty: MediumAccuracy: 34.65%Submissions: 216K+Points: 4
# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1. 

# Examples:

# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
# Input: s = "aaaa", k = 2
# Output: -1
# Explanation: There's no substring with 2 distinct characters.
# Input: s = "aabaaab", k = 2
# Output: 7
# Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
# Constraints:


def longestKSubstr(self, s, k):
        # code here
        max_len = -1
        start = 0
        freq ={}
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end],0) + 1
            
            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
            if len(freq) == k:
                max_len = max(max_len, end-start + 1)
            
        return max_len
    


print(longestKSubstr("aabacbebebe",3))