# Print 1 to n without using loops
# Difficulty: BasicAccuracy: 47.21%Submissions: 80K+Points: 1
# Given an positive integer n, print numbers from 1 to n without using loops.

# Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

# Examples

# Input: n = 5
# Output: 1 2 3 4 5
# Explanation: We have to print numbers from 1 to 5.
# Input: n = 10
# Output: 1 2 3 4 5 6 7 8 9 10
# Explanation: We have to print numbers from 1 to 10.
# Constraints:
# 1 ≤ n ≤ 1000



def printTillN(n, curr=1):
    if curr > n:
        return
    
    print(curr ,"")
    printTillN(n, curr + 1)



def printTillN1( N):
    #code here 
    if N == 0:
        return 
    printTillN1(N-1)
    print(N, end=" ")

# printTillN1(4)

def getNumbers(n):
    if n == 0:
        return []
    return getNumbers(n-1) + [n]

print(*getNumbers(5))

