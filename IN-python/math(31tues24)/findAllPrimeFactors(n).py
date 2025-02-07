# 285. Program to print all prime factors of a given number
# Numbertheory
# Google
# Amazon
# GoldmanSachs


# Given a number n, write an efficient function to print all prime factors of n. For example, if the input number is 12, then the output should be “2 2 3”. And if the input number is 315, then the output should be “3 3 5 7”.

# Input 1: 315
# Output 1: 3 3 5 7
# Explanation 1: Prime Factors of 315 are 3, 3, 5, 7

# Input 2: 12
# Output 2: 2 2 3
# Constraints:
# 1 <= N <= 106


def primeFactors(n):
    arr = []

    # for even 2 
    while n % 2==0:
        arr.append(2)
        n = n // 2
    # for odd 
    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            arr.append(i)
            n = n // i

    # for prime 
    if n>2:
        arr.append(n)
    
    return arr

print(primeFactors(15))