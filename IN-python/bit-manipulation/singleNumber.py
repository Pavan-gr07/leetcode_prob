# 136. Single Number
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


def singleNumber(arr):
    dict = {}
    ans =[]
    for i in range(len(arr)):
        dict[arr[i]] = dict.get(arr[i],0)+1
    print(dict)

    for x,y in dict.items():
        if y == 1:
            ans.append(x) 
    return ans
        

def usingBitManipulation(arr):
    result = 0
    for i in range(len(arr)):
        result ^= arr[i]
    return result


# def singleNumber1(nums) :
#     ones = 0
#     twos = 0

#     for num in nums:
#       ones ^= (num & ~twos)
#       twos ^= (num & ~ones)

#     return ones


print(singleNumber([1,2,1,3,2,5]))
# print(usingBitManipulation([2 ,1, 2, 2]))