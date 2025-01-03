# 245. Number of Good Pairs
# Array
# Amazon
# Nvidia


# Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Input 1: nums = [1,2,3,1,1,3]
# Output 1: 4
# Explanation 1: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Input 2: nums = [1,1,1,1]
# Output 2: 6
# Constraints:
# 1 <= nums.length <= 102
# 1 <= nums[i] <= 102


def goodPairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count +=1

    return count

print(goodPairs([1,1,1,1]))