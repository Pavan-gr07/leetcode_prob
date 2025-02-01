# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


def firstLastSorted(arr,target):
    if len(arr) ==1 and arr[0]==target:
        return 0
    start,end = 0,len(arr)
    while start<end:
        mid = (start+end)//2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid+1
    ans =[-1,-1]
    if start < len(arr) and arr[start] == target:
        ans[0]=start
        i=start+1
        while i<len(arr):
            if arr[i] == target:
                i+=1
            else:
                break
        ans[1] =i-1 
    return ans       


print(firstLastSorted([1,1,1],8))