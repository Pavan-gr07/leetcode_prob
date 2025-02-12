# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


def maxSubArray(nums,k):
    if len(nums) ==1:
        return nums[0]
    max_sum = float('-inf')
    for i in range(len(nums)-k+1):
        curr_sum =0
        for j in range(i,k+i):
            curr_sum += nums[j]
        max_sum = max(max_sum,curr_sum)
    return max_sum/k

print(maxSubArray([1,12,-5,-6,50,3],4))