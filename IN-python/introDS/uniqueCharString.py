# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Input 1: s = "leetcode"
# Output 1: 0
# Explanation 1: 'l' is the first non-repeating character in it which is present at index 0.

# Input 2: s = "loveleetcode"
# Output 2: 2
# Constraints:
# 1 <= s.length <= 105
# # s consists of only lowercase English letters.


def uniqueChar(s):
    temp = {}
    for ele in s:
        if ele in temp:
            temp[ele] +=1
        else:
            temp[ele] = 1
    for num in range(len(s)):
        if temp[s[num]] ==1:
            return num
    return -1
print(uniqueChar("dddccdbba"))