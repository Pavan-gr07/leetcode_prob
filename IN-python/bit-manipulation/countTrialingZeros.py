# 65. Count Trailing Zeroes
# Bitmanipulation
# Google
# Amazon
# Adobe


# Given an integer N, the task is to find the number of trailing zeroes in the 
# binary representation of the given number.

# Input 1: N = 12
# Output 1: 2
# Explanation 1: The binary representation of the number 13 is “1100”. 
# Therefore, there are two trailing zeros in the 12.

# Input 2: -56
# Output 2: 3
# Constraints:

def countTrialingZeros(n):
    count =0
    while n>0 and (n&1) == 0:
        count+=1
        n>>=1
      
    return count

print(countTrialingZeros(12))