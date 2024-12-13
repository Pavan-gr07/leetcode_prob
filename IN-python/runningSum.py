# 1480. Running Sum of 1d Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 


# def runningSum(arr):
#     temp = []
#     n = len(arr)
#     for i in range(0,n):
#         sum = 0 
#         for j in range(0,i+1):
#             sum = sum+arr[j]
#         print(sum)
#         temp.append(sum)
#     return temp
def runningSum(arr):
    temp = []
    current = 0
    for num in arr:
        current +=num
        temp.append(current)
    return temp



print(runningSum([1,1,1,1,1]))