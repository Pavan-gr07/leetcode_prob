# 107. Find largest prime factor of a number
# Numbertheory
# Mcafee


# Given a positive integer ‘N' ( 1 <= N <= 1015). Find the largest prime factor of a number.

# Input 1: 6
# Output 1: 3
# Explanation 1: Prime factor of 6 are - 2, 3
# Largest of them is '3'

# Input 2: 15
# Output 2: 5
# Constraints:
# 1 <= N <= 1015



def largestPrimeFact(n):
    large = None 
    
    while n % 2==0:
        large = 2
        n //= 2

    for i in range(3,int(n**0.5)+1,2):
        while n % i ==0:
            large = i
            n //= i
        
    if n>2:
        large = n
    return large

print(largestPrimeFact(15))