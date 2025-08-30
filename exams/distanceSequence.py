# 01. Distinct Subsequences
# DynamicProgramming
# Given two strings s and t, return the number of distinct subsequences of s which equals t.



# Input: s = "rabbbit", t = "rabbit"
# Output: 3

# Input: s = "babgbag", t = "bag"
# Output: 5

# Constraints:
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.class DistinctSubsequences:
def __init__(self, s, t):
    self.s = s
    self.t = t
    
def solve(self):
    m,n = len(self.s),len(self.t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    
    for i in range(1, m+1):
        for j in range(1,n+1):
            if self.s[i - 1] == self.t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]




# class DistinctSubsequences {
# public:
# 	int solve(string s1,string s2) {
#     		int n = s1.size(), m = s2.size();
#             vector> dp(n + 1, vector (m + 1, 0));

#             for (int i = 0; i < n + 1; i++)
#             {
#                 dp[i][0] = 1;
#             }
#             for (int i = 1; i < m + 1; i++)
#             {
#                 dp[0][i] = 0;
#             }

#             for (int i = 1; i < n + 1; i++)
#             {
#                 for (int j = 1; j < m + 1; j++)
#                 {

#                     if (s1[i - 1] == s2[j - 1])
#                         dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]);
#                     else
#                         dp[i][j] = dp[i - 1][j];
#                 }
#             }

#             return (int) dp[n][m];
#       }
# };
# Code for CSharp
# public class DistinctSubsequences
# {
#     public int Solve(string s, string t)
#     {
#         int m = s.Length, n = t.Length;

#         int[,] dp = new int[m + 1, n + 1];

#         // When target is empty, there's 1 subsequence for any source prefix
#         for (int i = 0; i <= m; i++)
#             dp[i, 0] = 1;

#         for (int i = 1; i <= m; i++)
#         {
#             for (int j = 1; j <= n; j++)
#             {
#                 if (s[i - 1] == t[j - 1])
#                 {
#                     dp[i, j] = dp[i - 1, j - 1] + dp[i - 1, j];
#                 }
#                 else
#                 {
#                     dp[i, j] = dp[i - 1, j];
#                 }
#             }
#         }

#         return dp[m, n];
#     }
# }