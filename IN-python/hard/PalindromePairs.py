# 336. Palindrome Pairs
# Hard
# Topics
# Companies
# Hint
# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a 
# palindrome
# .
# Return an array of all the palindrome pairs of words.

# You must write an algorithm with O(sum of words[i].length) runtime complexity.

 

# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]


def palindromePairs(arr):
    ans = []
    def pali1(str):
        left ,right = 0,len(str)-1
        while left <right:
            if str[left] != str[right]:
                return False
            left +=1
            right -=1
        return True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue
            new_str = arr[i]+arr[j]
            print(new_str)
            if pali1(new_str):
                ans.append([i,j])
    return ans
# TC - O(N^2)
# Sc  - O(N)
def palindromePairs1(arr):
    ans = []
    word_map = {word[::-1]: i for i, word in enumerate(arr)}  # Store reversed words

    def is_palindrome(s):
        return s == s[::-1]  # Faster palindrome check

    for i, word in enumerate(arr):
        for j in range(len(word) + 1):  # Split word at every position
            prefix, suffix = word[:j], word[j:]

            # Case 1: If prefix is a palindrome & reversed suffix exists
            if is_palindrome(prefix) and suffix in word_map and word_map[suffix] != i:
                ans.append([word_map[suffix], i])

            # Case 2: If suffix is a palindrome & reversed prefix exists
            if j != len(word) and is_palindrome(suffix) and prefix in word_map and word_map[prefix] != i:
                ans.append([i, word_map[prefix]])

    return ans

print(palindromePairs1(["abcd","dcba","lls","s","sssll"]))


