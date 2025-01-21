# 1582. Special Positions in a Binary Matrix
# Easy
# Topics
# Companies
# Hint
# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.

def specialPosBin(arr):
    count =0
    m = len(arr)
    n = len(arr[0])
    for row in range(m):
        for col in range(n):
            if arr[row][col] == 0:
                continue

            good = True
            # checking for the particular row
            for r in range(m):
                if r != row and arr[r][col] == 1:
                    good = False
                    break
            for c in range(n):
                if c != col and arr[row][c]==1:
                    good = False
                    break
            if good:
                count+=1


    return count

print(specialPosBin([[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]))



# class NumSpecial:
#     def __init__(self, mat):
#         self.mat = mat
        
#     def solve(self):
#         rows = [0] * len(self.mat)
#         cols = [0] * len(self.mat[0])
        
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[0])):
#                 if self.mat[i][j] == 1:
#                     rows[i] += 1
#                     cols[j] += 1
        
#         res = 0
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[0])):
#                 if self.mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
#                     res += 1
        
#         return res