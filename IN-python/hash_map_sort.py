# 338. Sort Array by Increasing Frequency
# Array
# Hashing
# Oracle
# Amazon
# Microsoft
# +


# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.



# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]


# steps
# dic ={
#     1:2,
#     2:3,
#     3:1
# }

# items = list(dic.items())#[(3, 1), (1, 2), (2, 3)]

# # Bubble sort the list based on values
# n = len(items)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if items[j][1] > items[j+1][1]:  # Compare values
#             items[j], items[j+1] = items[j+1], items[j]

# # Rebuild the dictionary from the sorted list
# sorted_dic = {key: value for key, value in items}
# arr = []
# for elem in sorted_dic:
#     arr.append(elem)
# print(arr)



def frequency_sort(nums):
    # Step 1: Count the frequency of each element
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    print(freq)
    
    # Step 2: Sort the array by frequency, then by value in descending order for ties
    nums.sort(key=lambda x: (freq[x], -x))
    
    return nums

# Example usage:
nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [2, 3, 1, 3, 2]

print(frequency_sort(nums1))  # Output: [3, 1, 1, 2, 2, 2]
# print(frequency_sort(nums2))  # Output: [1, 3, 3, 2, 2]

# def HashMapSort(arr):

#     return 0
    
# print(HashMapSort([1,1,2,2,2,3]))