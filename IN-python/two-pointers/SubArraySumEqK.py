# 560. Subarray Sum Equals K
# Medium
# Topics
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



# def subArrayEqK(arr,target):
#     if len(arr)==0: return 0
#     if len(arr) == 1 and arr[0]!=target: return 0
#     left,right = 0,len(arr)-1

#     count = 0
#     while left < right:
#         sumValue  = arr[left] + arr[right]
#         if sumValue == target:
#             count += 1
#             left+=1
#             right -=1
#         else:
#             if sumValue < target:
#                 left += 1
#             else:
#                 right -= 1
#     return count+1

# print(subArrayEqK( [1,2,1,2,1],3))


def subarraySumBrute(nums, k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == k:
                count +=1
    return count

print(subarraySumBrute([1,2,1,2,1], 3))

def subarraySum(nums, k):
    prefix_count = {0: 1}  # Base case: A sum of 0 appears once initially.
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num  # Update running sum

        if (prefix_sum - k) in prefix_count:  # Check if we found a valid subarray
            count += prefix_count[prefix_sum - k]

        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1  # Store the sum count

    return count

# TC(O(n))
# Test Case
print(subarraySum([1,2,3], 3))  # Expected Output: 4
