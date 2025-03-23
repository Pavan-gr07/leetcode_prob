# 17. Letter Combinations of a Phone Number
# Medium
# Topics
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.4M
# Submissions
# 3.9M
# Acceptance Rate
# 63.2%


def letterCombinationPhoneNo(str):
    dict = {
        "2":'abc',
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    if not str:
        return []

    temp = []
    for ele in str:
        if dict[ele]:
            temp.append(dict[ele])

    ans = []
    if len(temp)==1:
        for ele in temp[0]:
            ans.append(ele)
    elif len(temp)==2:
        for ele in temp[0]:
            for j in temp[1]:
                ans.append(ele+j)
    elif len(temp)==3:
        for ele in temp[0]:
            for j in temp[1]:
                for k in temp[2]:
                    ans.append(ele+j+k)
    elif len(temp)==4:
        for ele in temp[0]:
            for j in temp[1]:
                for k in temp[2]:
                    for l in temp[2]:
                        ans.append(ele+j+k+l)
    return ans

# TC - O(4^N)
# from typing import List
def letterCombinations( digits) :
        if not digits:
            return []
        
        digit_to_chars = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        ans = []

        def backtrack(index, path):
            if index == len(digits):
                ans.append("".join(path))
                return
            
            for char in digit_to_chars[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()  # Backtrack step
        
        backtrack(0, [])
        return ans


""" efficient method is backtracking approach"""
print(letterCombinations("23"))


# "" (start)
# ├── "a"
# │   ├── "ad"
# │   ├── "ae"
# │   ├── "af"
# ├── "b"
# │   ├── "bd"
# │   ├── "be"
# │   ├── "bf"
# └── "c"
#     ├── "cd"
#     ├── "ce"
#     ├── "cf"
