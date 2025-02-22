# 73. Set Matrix Zeroes
# Medium
# Topics
# Companies
# Hint
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


def matrixZeros(arr):
    row = len(arr)
    col = len(arr[0])
    index_arr = []
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                index_arr.append([i,j])

 # O(M*N)

    for ele in index_arr:
        for k in range(col):
            arr[ele[0]][k] =0
        for l in range(row):
            arr[l][ele[1]] =0


    return arr

print(matrixZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))