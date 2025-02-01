# 33. Search in Rotated Sorted Array
# Medium
# Topics
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000


def searchInRottedSorted(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

# TC-O(len(arr)) -O(n)

# Reducing to log(n)
# Since the array is **sorted but rotated**, you can use **binary search** to reduce the time complexity to **\(O(\log n)\)** instead of \(O(n)\). The key idea is to identify the **pivot point** (the rotation index) while performing binary search. 

# ### Optimized \(O(\log n)\) Binary Search Approach:
# ```python
# from typing import List

def search(nums, target) :
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # If the mid element is the target, return its index
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:  # Target lies in this range
                right = mid - 1
            else:
                left = mid + 1  # Search in the right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:  # Target lies in this range
                left = mid + 1
            else:
                right = mid - 1  # Search in the left half

    return -1  # Target not found
# ```

# ### Explanation:
# 1. **Binary Search**: The algorithm maintains `left` and `right` pointers and repeatedly halves the 
# search space.
# 2. **Check which half is sorted**:
#    - If `nums[left] <= nums[mid]`, it means the **left half** is sorted.
#    - Otherwise, the **right half** is sorted.
# 3. **Determine where the target lies**:
#    - If the **target lies in the sorted half**, adjust `left` or `right` accordingly.
#    - Otherwise, search in the other half.
# 4. **Return index if found**, else return `-1`.

# ### Time Complexity:
# - **\(O(\log n)\)** since we eliminate half of the array in each step.

# This approach is much more efficient than a linear search and works optimally for rotated sorted arrays. 🚀

print(searchInRottedSorted([4,5,6,7,0,1,2],3))