# Search Element in a Rotated Sorted Array

# Mark as Completed

# 314


# Problem Statement: Given an integer array arr of size N, sorted in ascending order 
# (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you.
#  Find the index at which k is present and if k is not present return -1.

# Examples

# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
# Result: 4
# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array,
#  nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

# Example 2:
# Input Format: arr = [4,5,6,7,0,1,2], k = 3
# Result: -1
# Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array.
#  Thus, we get the output as -1.


def searchElement(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) // 2


        if arr[mid] == target:
            return mid
        
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid -1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(searchElement([4,5,6,7,0,1,2,3],0))


