# 312. Burst Balloons
# Hard
# Topics
# premium lock icon
# Companies
# You are given n balloons, indexed from 0 to n - 1. Each balloon is 
# painted with a number on it represented by an array nums. 
# You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
#  If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 10


def maxCoins(nums):
    # Pad the nums array with 1 at both ends
    nums = [1] + nums + [1]
    n = len(nums)
    
    # dp[i][j] = max coins from bursting balloons between i and j (exclusive)
    dp = [[0] * n for _ in range(n)]
    
    # len is the length of the window we consider
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            # Try bursting each balloon in (left, right)
            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]
                coins += dp[left][k] + dp[k][right]
                dp[left][right] = max(dp[left][right], coins)

    return dp[0][n - 1]


print(maxCoins([3,1,5,8]))