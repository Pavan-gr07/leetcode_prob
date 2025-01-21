# 74. Search a 2D Matrix
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


def search2DMat(arr):
    row = len(arr)
    col = len(arr[0])
    target = 3
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(arr[i][j])
        start = temp[0]
        end = temp[len(temp)-1]
        if start <= target or end >= target:
            for ele in temp:
                if ele == target:
                    return True
    return False            
        

print(search2DMat([[1,3,5,7],[10,11,16,20],[23,30,34,60]]))