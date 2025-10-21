# Stream First Non-repeating
# Difficulty: Medium Accuracy: 31.65%Submissions: 224K+Points: 4Average Time: 15m
# Given a string s consisting of only lowercase alphabets, for each index i in the string (0 ≤ i < n), find the first non-repeating character in the prefix s[0..i]. If no such character exists, use '#'.

# Examples:

# Input: s = "aabc"
# Output: a#bb
# Explanation: 
# At i=0 ("a"): First non-repeating character is 'a'.
# At i=1 ("aa"): No non-repeating character, so '#'.
# At i=2 ("aab"): First non-repeating character is 'b'.
# At i=3 ("aabc"): Non-repeating characters are 'b' and 'c'; 'b' appeared first, so 'b'. 
# Input: s = "bb" 
# Output: "b#" 
# Explanation: 
# At i=0 ("b"): First non-repeating character is 'b'.
# At i=1 ("bb"): No non-repeating character, so '#'.

# Constraints:
# 1 ≤ s.size() ≤ 105

from collections import deque

def firstNonRepeating(stream):
    freq = {}
    q = deque()
    result = []

    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        # Remove all repeating chars from front
        while q and freq[q[0]] > 1:
            q.popleft()

        if q:
            result.append(q[0])
        else:
            result.append("-1")
    
    return result

# Example usage
stream = ['a', 'a', 'b', 'c']
print(firstNonRepeating(stream))  # ['a', '-1', 'b', 'b']


stream = ["a","b","b","a"]
print(firstNonRepeating(stream))