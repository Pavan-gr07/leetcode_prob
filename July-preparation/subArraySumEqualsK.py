# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 


def subArraySumEqualsK(arr,k):
    count = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i,len(arr)):
            total += arr[j]
            if total == k:
                count += 1

    return count
# TC - O(N^2)
# SC - O(1)



def subArraySumEqualsKOptimize(arr,k):
    count = 0
    cur_sum = 0
    dict ={0:1}
    
    
    for i in range(len(arr)):
        cur_sum += arr[i]
        count += dict.get(cur_sum - k,0) 
        dict[cur_sum] = dict.get(cur_sum, 0) + 1


    return count
# TC - O(N)
# SC - O(1)
print(subArraySumEqualsKOptimize([1,2,3],3))