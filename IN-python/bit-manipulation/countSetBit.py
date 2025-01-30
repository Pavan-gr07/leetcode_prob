n = 11 # 1 1 0 0 1 1


count = 0
while n > 0:
    count += n&1
    n >>= 1

print(count)