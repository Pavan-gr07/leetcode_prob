
# We are given a square matrix mat. Our task is to return the sum of the elements on the primary and secondary diagonals without counting any element twice (if it occurs on both the diagonals).
# Given a square matrix mat, return the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Input 1: mat = [[1,2,3], [4,5,6], [7,8,9]]
# Output 1: 25
# Explanation 1: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25. Notice that element mat[1][1] = 5 is counted only once.

# Input 2: mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
# Output 2: 8
# Constraints:
# n == mat.length, mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100




def matrixDiagonalSum(mat):
    n = len(mat)
    ans = 0
    for i in range(n):
        ans += mat[i][i]
        ans += mat[n-1-i][i]
    if n % 2 != 0:
        ans -= mat[n // 2][n // 2]
    return ans


print(matrixDiagonalSum([[1,2,3],[4,5,6],[7,8,9]]))