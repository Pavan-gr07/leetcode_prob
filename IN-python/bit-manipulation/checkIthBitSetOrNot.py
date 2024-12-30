n = 105 # 1 1 0 0 1 1
# 1010
ith = 5  #


# mask = 1 << (ith-1) #
# ans = n& mask

# if ans != 0:
#     print(True)
# else:
#     print(False)


if n >> ith & 1:
    print(True)
else:
    print(False)