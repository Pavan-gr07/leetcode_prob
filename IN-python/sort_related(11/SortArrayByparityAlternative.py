# 922. Sort Array By Parity II
# Easy
# Topics
# Companies
# Given an array of integers nums, half of the integers in nums are odd, and the 
# other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever 
# nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

 

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

def sortArrayByParity2(arr):
    ans = [0]*len(arr)
    even_idx,odd_idx = 0,1
    for ele in arr:
        if ele % 2 == 0:
            ans[even_idx] = ele
            even_idx += 2
        else:
            ans[odd_idx] = ele
            odd_idx += 2

    return ans


print(sortArrayByParity2([4,2,5,7]))
