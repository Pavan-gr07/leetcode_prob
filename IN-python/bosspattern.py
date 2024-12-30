# Input 1: N = 4
# Output 1:
# a
# ab
# abc
# abcd

def pat3(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('a')+j),end="")
        print()

# print(pat3(5))




# Print the Hollow Square Star Pattern for the given value of N.
# Input 1: N = 4
# Output 1:
# ****
# *__*
# *__*
# ****
# Explanation 1: Square of 4*4 will be formed with 4 star in first row from the beginning, one star in second row from the beginning and one star in the second row from the last and so on.
# Input 2: N = 3
# Output 2:
# ***
# *_*
# ***
# Constraints:
# 1 <= N <= 10


def pat4(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i == n-1 or j==0 or j == n-1:
                print("*",end="")
            else:
                print("-",end="")
        print("")
pat4(4)