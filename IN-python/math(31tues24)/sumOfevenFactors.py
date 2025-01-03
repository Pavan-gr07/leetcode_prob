#  Find sum of even factors of a number
# Numbertheory
# Jp Morgan


# Given a number N, the task is to find the even factor sum of a number.

# Input 1: 30
# Output 1: 48
# Explanation 1: Even dividers sum 2 + 6 + 10 + 30 = 48

# Input 2: 18
# Output 2: 26
# Constraints:
# 1 <= N <= 106


def evenSumFactors(n):
    sum = 0
    for i in range(1,int(n**0.5)+1):
        if n % i ==0:
            if i % 2==0:
                sum = sum + i
            if i != n // i and (n // i) % 2==0:
                sum = sum + (n//i)
    return sum

print(evenSumFactors(18))

