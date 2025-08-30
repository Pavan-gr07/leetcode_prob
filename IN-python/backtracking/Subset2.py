# 90. Subsets II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


def subsetsWithDup(nums):
    nums.sort()
    res = []
    def backtrack(s,path):
        res.append(path[:])
        for i in range(s, len(nums)):
            if i > s and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res


print(subsetsWithDup([1,2,2]))