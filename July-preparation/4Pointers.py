# 18. 4Sum

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]






def fourSum(arr,target):
    arr.sort()
    unique = set()
    ans = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,len(arr)):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            left = j + 1 
            right = len(arr) - 1
            while left < right:
                sum_val = arr[i] + arr[j] + arr[left] + arr[right]
                if sum_val == target:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif sum_val < target:
                    left += 1
                else:
                    right -= 1
                    
    return ans

# TC - O(n^3)
# SC - O(n)



print(fourSum([1,0,-1,0,-2,2],0))