# 125. Four Divisors
# Array
# Maths
# SAP
# Paytm


# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Input 1: nums = [21,4,7]
# Output 1: 32
# Explanation 1: 21 has 4 divisors: 1, 3, 7, 21. 4 has 3 divisors and 7 has 2 divisors. The answer is the sum of divisors of 21 only.

# Input 2: nums = [21,21]
# Output 2: 64
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 1 <= nums[i] <= 105

def fourDivisors(arr):
    sum=0

    for i in range(len(arr)):
        sum += helper(arr[i])
    return sum

def helper(n):
    arr = []
    for i in range(1,n+1):  
        if n % i ==0:
            arr.append(i)
    if len(arr) == 4:
        return sum(arr)
    else:
        return False

print(fourDivisors([1,2,3,4,5]))