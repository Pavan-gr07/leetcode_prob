# 189. Rotate Array
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps,
# 
# 
#  where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


def rotateArray(arr,k):
    while k>0:
        arr=[arr[-1]]+arr[:-1]   #here it is creating one more list not modifying in-place so
        k-=1

    return arr
def rotateArrayInPlace(arr,k):
    while k>0:
        last = arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last
        k-=1

    return arr
# above time limit exceed error came TC O(nk)
def rotateArrayInBestTC(arr,k):
    n = len(arr)
    print(k%n)
    k %= n  # Avoid unnecessary full rotations
    arr[:] = arr[-k:] + arr[:-k] 
    return arr
    # cutting and pasting

# TC-(O(nj))

print(rotateArrayInBestTC([1,2,3,4,5,6,7],12))