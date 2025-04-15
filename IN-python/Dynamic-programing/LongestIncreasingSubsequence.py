
# Code
# Testcase
# Test Result
# Test Result
# 300. Longest Increasing Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


def lengthOfLIS( nums):
        dp = [0]*len(nums)

        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i] :
                    dp[i] = dp[j] + 1

        return max(dp)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))