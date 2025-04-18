# 540. Single Element in a Sorted Array
# Solved
# Medium
# Topics
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

# Intuition of this Problem:
# Since every element in the sorted array appears exactly twice except for the single element, we know that 
# if we take any element at an even index (0-indexed), the next element should be the same. 
# Similarly, if we take any element at an odd index, the previous element should be the same.
#  Therefore, we can use binary search to compare the middle element with its adjacent elements
#  to determine which side of the array the single element is on.

# If the middle element is at an even index, then the single element must be on the right side of the array, 
# since all the elements on the left side should come in pairs. Similarly, if the middle element is at an odd 
# index, then the single element must be on the left side of the array.

# We can continue this process by dividing the search range in half each time, until we find the single 
# element.

# Another interesting observation you might have made is that this algorithm will still work even 
# if the array isn't fully sorted. As long as pairs are always grouped together in the array (for example,
#  [10, 10, 4, 4, 7, 11, 11, 12, 12, 2, 2]), it doesn't matter what order they're in. Binary search worked 
# for this problem because we knew the subarray with the single number is always odd-lengthed, not because 
# the array was fully sorted numerically

# NOTE - PLEASE READ APPROACH FIRST THEN SEE THE CODE. YOU WILL DEFINITELY UNDERSTAND THE CODE
#  LINE BY LINE AFTER SEEING THE APPROACH.

# Approach for this Problem:
# Initialize two pointers, left and right, to the first and last indices of the input array, respectively.
# While the left pointer is less than the right pointer:
# a. Compute the index of the middle element by adding left and right and dividing by 2.
# b. If the index of the middle element is odd, subtract 1 to make it even.
# c. Compare the middle element with its adjacent element on the right:
# i. If the middle element is not equal to its right neighbor, the single element must be on the left side of the array, so update the right pointer to be the current middle index.
# ii. Otherwise, the single element must be on the right side of the array, so update the left pointer to be the middle index plus 2.
# When the left and right pointers converge to a single element, return that element.
# Code:
def singleNonDuplicate( nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
# Time Complexity and Space Complexity:
# Time complexity: O(logn)
# Space complexity: O(1)