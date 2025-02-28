# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# TC - O(N^3)
def maxSumSubArray(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            cur_sum = 0
            for k in range(j,n):
                cur_sum += arr[k]
                max_sum = max(cur_sum,max_sum)

    return max_sum
# TC - O(N^2)
def maxSumSubArray2(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            max_sum = max(cur_sum,max_sum)

    return max_sum
# TC - O(N)
def maxSumSubArray3(arr):
    cur_sum = 0
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        cur_sum += arr[i]
        max_sum = max(cur_sum,max_sum)
        if cur_sum < 0:
            cur_sum = 0

    return max_sum


print(maxSumSubArray3([-2,1,-3,4,-1,2,1,-5,4]))

