n = 105
# 1010
ith = 5


mask = 1 << (ith-1)
ans = n ^ mask

print(ans)
