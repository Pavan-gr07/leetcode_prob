mat = [[1,1, 0], [0, 1, 1], [1, 0, 1]]


col = len(mat[0])
row = len(mat)


mod = []
# flip
for i in range(0,row):
    row = []
    for j in range(0,col):
        print(col-j-1)
        row.append(1-mat[i][(col-j)-1]) 
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