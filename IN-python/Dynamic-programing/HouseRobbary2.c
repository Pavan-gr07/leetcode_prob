# 213. House Robber II
# Medium
# Topics
# Companies
# Hint
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3


class Solution {
public:
    int solve(int i, vector<int>& nums, vector<int>& dp) {
        if (i >= nums.size()) {
            return 0;
        }
        if (dp[i] != -1) {
            return dp[i];
        }

        int take = nums[i] + solve(i+2, nums, dp);
        int dont = solve(i+1, nums, dp);

        return dp[i] = max(take, dont);
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        vector<int> dp1(n-1, -1);
        vector<int> dp2(n-1, -1);

        vector<int> temp1;
        for (int i = 1; i < n; i++) {
            temp1.push_back(nums[i]);
        }
        vector<int> temp2;
        for (int i = 0; i < n-1; i++) {
            temp2.push_back(nums[i]);
        }

        return max(solve(0, temp1, dp1), solve(0, temp2, dp2));
    }
};
