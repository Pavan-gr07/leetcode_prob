# 2461. Maximum Sum of Distinct Subarrays With Length K
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:

# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.
 

# Constraints:

# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 105



def maxSumDistictSubArr(arr,k):
    max_sum =0
    cur_sum =0
    for i in range(len(arr)):
        unique_ele = set(arr[i:k+i])
        if len(unique_ele) == k:
            cur_sum = sum(unique_ele)
            max_sum = max(cur_sum,max_sum)
    return max_sum

# Tc - O(n*k)
# Problems in Your Code
# nums[i:k+i] creates a new list slice on every iteration

# Slicing (nums[i:k+i]) takes O(K) time complexity.
# In the worst case, you do this O(N) times, making it O(N * K).
# set(nums[i:k+i]) takes additional O(K) time

# Creating a set takes O(K).
# Since you’re calling it inside an O(N) loop, the overall complexity becomes O(N * K).
# Using sum(unique_ele) in every iteration is O(K)

# Instead of maintaining a running sum, you're recalculating it every time, adding another O(K) factor.
print(maxSumDistictSubArr([4,4,4],3))