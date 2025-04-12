# 64. Minimum Path Sum
# Solved
# Medium
# Topics
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200

# 0 <= grid[i][j] <= 200

def minPathSum( grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    def solve(i,j):
        if i == m-1 and j == n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return float('inf')
        if  dp[i][j] != -1:
            return dp[i][j] 
        down= solve(i+1,j)
        right = solve(i,j+1)
        dp[i][j] = grid[i][j] + min(down,right)
        return dp[i][j]
    return solve(0,0)





print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))