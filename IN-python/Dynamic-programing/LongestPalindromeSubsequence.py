# 516. Longest Palindromic Subsequence
# Solved
# Medium
# Topics
# Companies
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1=s
        text2 = s[::-1]
        i=len(text1)-1
        j=len(text2)-1
        dp = [[-1 for _ in range(j+1)] for _ in range(i+1)]

        def modify(i,j):
            if i<0:
                return 0
            if j<0:
                return 0

            if dp[i][j] != -1: return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + modify(i-1,j-1)
                return dp[i][j]
            else:
                # insert
                s1 = modify(i,j-1)
                # remove
                s2 =  modify(i-1,j)
                # replace
                dp[i][j] = max(s1,s2)
                return dp[i][j]

        return modify(i,j)