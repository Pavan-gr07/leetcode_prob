
# 832. Flipping an Image
# Solved
# Easy
# Topics
# Companies
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

# For example, inverting [0,1,1] results in [1,0,0].
 

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

# Constraints:

# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.









mat = [[1,1, 0], [0, 1, 1], [1, 0, 1]]


col = len(mat[0])
row = len(mat)


mod = []
# flip
for i in range(0,row):
    row = []
    for j in range(0,col):
        print(col-j-1)
        row.append(mat[i][(col-j)-1]) 
    mod.append(row)
# # # inversion
# col = len(mod[0])
# row = len(mod)
# for i in range(0,row):
#     for j in range(0,col):
#         if mod[i][j]==0:
#             mod[i][j]=1
#         else:
#             mod[i][j]=0
print(mod)