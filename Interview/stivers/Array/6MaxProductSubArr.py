# Maximum Product Subarray in an Array

# Mark as Completed

# 281


# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

# Examples

# Example 1:
# Input:
#  Nums = [1,2,3,4,5,0]
# Output:
#  120
# Explanation:
#  In the given array, we can see 1×2×3×4×5 gives maximum product value.


# Example 2:
# Input:
#  Nums = [1,2,-3,0,-4,5]
# Output:
#  20
# Explanation:
#  In the given array, we can see (-4)×(-5) gives maximum product value.


def maxProductSubArr(arr):
    if len(arr) ==1:
        return arr[0]
    max_val = 0
    cur_max  = 1
    cur_min  = 1



    for ele in arr:
        temp_min = cur_min
        temp_max = cur_max
        cur_max = max(ele, temp_max*(ele), temp_min*(ele))
        cur_min = min(ele, temp_max*(ele), temp_min*(ele))
        max_val = max(max_val, cur_max)
        if cur_max == 0:
            cur_max = 1
        
    return max_val

print(maxProductSubArr([-4,-3,-2]))

# [3,-1,4]
# [2,3,-2,4]
# [-2,0,-1]
# [1,2,-3,0,-4,-5]
# [-4,-3,-2]