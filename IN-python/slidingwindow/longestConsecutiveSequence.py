# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 



def longestConsecutiveSentence(nums):
    max_count =0
    nums = set(nums)
    cur_sum = 0
    count =0
    for num in nums:
        if num -1 not in nums:
            cur_sum= num
            count = 1
            while cur_sum+1 in nums:
                cur_sum += 1
                count += 1
            max_count = max(count,max_count)

    return max_count

print(longestConsecutiveSentence([100,4,200,1,3,2]))