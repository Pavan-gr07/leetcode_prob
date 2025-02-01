# 704. Binary Search
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

def binarySearch(arr,target):
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
        return start
    else:
        return -1     
    
        
print(binarySearch([5,7,7,8,8,10],8))