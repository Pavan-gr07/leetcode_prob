# 4. Median of Two Sorted Arrays

# avatar
# Discuss Approach
# arrow-up
# Hard
# Topics
# premium lock icon
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106



def medianOfTwoSortedArr(nums1,nums2):
    ans = 0
    
    mergeArr = []
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)

    # Function to merge two sorted arrays
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    mergeArr = mergeSort(nums1+nums2)
    n = len(mergeArr)
    if( n% 2 == 0):
        ans = (mergeArr[n // 2 - 1] + mergeArr[n // 2]) / 2
    else:
        ans = mergeArr[n // 2]

    return ans

print(medianOfTwoSortedArr([1,3],[2]))