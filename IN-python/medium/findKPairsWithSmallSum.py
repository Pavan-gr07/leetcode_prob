# 373. Find K Pairs with Smallest Sums
# Medium
# Topics
# Companies
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length

def KPairsSmallestSum(arr1,arr2,k):
    ans = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            ans.append([arr1[i],arr2[j]])

    # here need to sort based on the sum values this gone
    return ans[:k]
# TC - O(N*N) + O(nlog(N))
# Sc - O(N)

import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []
    
    # Min-heap to store pairs (sum, num1, num2, index1, index2)
    min_heap = []
    
    # Initialize with the first column of nums1 paired with each element of nums2
    for j in range(min(k, len(nums2))):
        heapq.heappush(min_heap, (nums1[0] + nums2[j], nums1[0], nums2[j], 0, j))
    
    result = []
    
    # Pop the smallest k pairs
    while min_heap and len(result) < k:
        current_sum, num1, num2, i, j = heapq.heappop(min_heap)
        result.append([num1, num2])
        
        # Push the next pair (nums1[i+1], nums2[j]) if nums1 has more elements
        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], nums1[i + 1], nums2[j], i + 1, j))
    
    return result



print(k_smallest_pairs([1,3,5],[2,4,6],4))