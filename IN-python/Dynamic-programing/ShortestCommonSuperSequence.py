# Shortest Common Supersequence
# Difficulty: MediumAccuracy: 55.62%Submissions: 128K+Points: 4
# Given two strings s1 and s2, find the length of the smallest string which has both s1 and s2 as its sub-sequences.
# Note: s1 and s2 can have both uppercase and lowercase English letters.

# Examples:

# Input: s1 = "geek", s2 = "eke"
# Output: 5
# Explanation: String "geeke" has both string "geek" and "eke" as subsequences.
# Input: s1 = "AGGTAB", s2 = "GXTXAYB"
# Output: 9
# Explanation: String "AGXGTXAYB" has both string "AGGTAB" and "GXTXAYB" as subsequences.
# Input: s1 = "geek", s2 = "ek"
# Output: 4
# Explanation: String "geek" has both string "geek" and "ek" as subsequences.
# Constraints:
# 1<= s1.size(), s2.size() <= 500

# Expected Complexities

def shortestCommonSupersequence(self, s1, s2):
        def longestCommonSubsequence(text1, text2):
            i = len(text1)
            j = len(text2)
            dp = [[-1 for _ in range(j)] for _ in range(i)]
    
            def modify(i, j):
                if i < 0 or j < 0:
                    return 0
    
                if dp[i][j] != -1:
                    return dp[i][j]
    
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + modify(i - 1, j - 1)
                else:
                    dp[i][j] = max(modify(i, j - 1), modify(i - 1, j))
                return dp[i][j]
    
            return modify(i - 1, j - 1)
    
        a = len(s1)
        b = len(s2)
        lcs_len = longestCommonSubsequence(s1, s2)
        return a + b - lcs_len