# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# Examples
# Example 1:

# Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output: 6 

# Explanation: [4,-1,2,1] has the largest sum = 6. 

# Examples 2: 

# Input: arr = [1] 

# Output: 1 

# Explanation: Array has only one element and which is giving positive sum of 1. 


def kadanesAlgo(arr):
    max_val = 0
    cur_sum = 0 

    for ele in arr:
        cur_sum += ele
        max_val = max(max_val,cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_val


print(kadanesAlgo([-2,1,-3,4,-1,2,1,-5,4]))