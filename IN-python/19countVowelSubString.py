# 2062. Count Vowel Substrings of a String
# Easy
# Topics
# Companies
# Hint
# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

 

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# Example 2:

# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
# Example 3:

# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase English letters only.









def countVowelSubString(str):
    count = 0
    length = len(str)
    for i in range(0,length):
        vowel = [0]*5
        for j in range(i,length):
            if str[j] == 'a':
                vowel[0] += 1
            elif str[j] == 'e':
                vowel[1] += 1
            elif str[j] == 'i':
                vowel[2] += 1
            elif str[j] == 'o':
                vowel[3] += 1
            elif str[j] == 'u':
                vowel[4] += 1
            else: break
            if check(vowel): count += 1

    return count

def check(arr):
    for i in arr:
        if i==0:
            return False
            
    return True



print(countVowelSubString("aeiouu"))




# class Solution(object):
#     def countVowelSubstrings(self, word):
#         """
#         :type word: str
#         :rtype: int
#         """
#         def is_vowel(ch):
#             return ch in "aeiou"
#         count = 0
#         n = len(word)
#         for i in range(n):
#             vowels_seen = set()
#             for j in range(i, n):
#                 if is_vowel(word[j]):
#                     vowels_seen.add(word[j])
#                     if len(vowels_seen) == 5:  # All vowels present
#                         count += 1
#                 else:
#                     break  # Stop if a non-vowel character is encountered
                
#         return count
