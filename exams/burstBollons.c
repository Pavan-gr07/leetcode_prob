// 01. Burst Balloons
// DynamicProgramming
// You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

// If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

// Return the maximum coins you can collect by bursting the balloons wisely.

// Input: nums = [3,1,5,8]
// Output: 167
// Explanation:
// nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
// coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

// Input: nums = [1,5]
// Output: 10

// Constraints:
// n == nums.length
// 1 <= n <= 300
// 0 <= nums[i] <= 100

// class BurstBalloons{
//     public :
//         int solve(vector<int> input){
//             int n = input.size();

// vector<int> ballons(n + 2, 1);
// for (int i = 0; i < n; ++i)
// {
//     ballons[i + 1] = input[i];
// }

// vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));

// for (int length = 2; length <= n + 1; ++length)
// {
//     for (int left = 0; left <= n + 1 - length; ++left)
//     {
//         int right = left + length;
//         for (int k = left + 1; k < right; ++k)
//         {
//             int coins = ballons[left] * ballons[k] * ballons[right];
//             coins += dp[left][k] + dp[k][right];
//             dp[left][right] = max(dp[left][right], coins);
//         }
//     }
// }
// return dp[0][n + 1];
// }
// }
// ;