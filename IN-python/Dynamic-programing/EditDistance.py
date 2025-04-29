# 72. Edit Distance
# Medium
# Topics
# Companies
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.



def EditDistance(word1,word2):
    i=len(word1)-1
    j=len(word2)-1
    dp = [[-1 for _ in range(j+1)] for _ in range(i+1)]

    def modify(i,j):
        if i<0:
            return j+1
        if j<0:
            return i+1
        
        if dp[i][j] != -1: return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = 0 + modify(i-1,j-1)
            return dp[i][j]
        else:
            # insert
            s1 = 1 + modify(i,j-1)
            # remove
            s2 = 1 + modify(i-1,j)
            # replace
            s3 = 1 + modify(i-1,j-1)
            dp[i][j] = min(s1,min(s2,s3))
            return dp[i][j]
        
    return modify(i,j)


print(EditDistance("horse","ros"))
