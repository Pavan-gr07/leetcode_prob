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


def longestConsectiveSequence(nums):
    if not nums:
            return 0  # Edge case: empty numsay

    nums = set(nums)  # Remove duplicates
    max_count = 0  # Track the longest sequence length
    for num in nums:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in nums:  
            current_num = num
            count = 1  # Start new sequence
            while current_num + 1 in nums:
                current_num += 1
                count += 1
            max_count = max(max_count, count)  # Update longest sequence length
    return max_count


print(longestConsectiveSequence([-1,0,1,3,4,5,6,7,8,9]))