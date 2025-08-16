# Problem: Maximum Size Subarray with Sum ≤ K
# Given an array of integers arr and an integer k, return the length of the longest subarray whose sum is less than or equal to k.

# Example:
# python
# Copy
# Edit
# Input: arr = [1, 2, 3, 4, 5], k = 8  
# Output: 3  
# # Because [1,2,3] → sum = 6 and [2,3,4] = 9 (too large), [3,4] = 7, but 


def maxSubArrayLenWithSumAtMostK(arr, k):
    start = 0
    cur_sum = 0
    max_len = 0

    for end in range(len(arr)):
        cur_sum += arr[end]
        
        while cur_sum > k:
            cur_sum -= arr[start]
            start += 1
        
        # This is where you had a small typo: right-left+1 -> end-start+1
        max_len = max(max_len, end - start + 1)

    return max_len

from bisect import bisect_left, insort


def max_subarray_len(arr, k):
    prefix_sum = 0
    prefix_sums = [0]
    result = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]
        # Find smallest prefix_sum[i] >= prefix_sum - k
        idx = bisect_left(prefix_sums, prefix_sum - k)
        if idx < len(prefix_sums):
            result = max(result, i - idx + 1)
        insort(prefix_sums, prefix_sum)

    return result


print(max_subarray_len([3,-2,5,-1],5))