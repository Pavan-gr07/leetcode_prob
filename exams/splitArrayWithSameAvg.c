// # 1. Split Array With Same Average
// # DynamicProgramming
// # You are given an integer array nums. You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B). Return true if it is possible to achieve that and false otherwise.

// # Input: nums = [1,2,3,4,5,6,7,8]
// # Output: true
// # Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

// # Input: nums = [3,1]
// # Output: false

// # Constraints:
// # 1 <= nums.length <= 30
// # 0 <= nums[i] <= 104

// class ArraySplitSameAverage
// {
// public:

//     unordered_map mp;

//     bool helper(vector & nums, int i, int n, int sum, int n1)
//     {
//         // base case

//         if (n1 == 0)
//             return sum == 0;

//         if (i == n)
//             return false;

//         // create a key

//         string key = to_string(i) + "#" + to_string(n1) + "#" + to_string(sum);

//         // if already calculated

//         if (mp.count(key))
//             return mp[key];

//         // if nums[i] <= sum, then we will either include or exclude

//         // calculate the result and store in map

//         if (nums[i] <= sum)
//         {
//             return mp[key] = helper(nums, i + 1, n, sum - nums[i], n1 - 1) || helper(nums, i + 1, n, sum, n1);
//         }
//         else
//             return mp[key] = helper(nums, i + 1, n, sum, n1);
//     }

//     bool check(vector nums)
//     {
//         int n = nums.size();

//         // find the total sum

//         int sum = 0;

//         for (int i = 0; i < n; i++)
//         {
//             sum += nums[i];
//         }

//         // check for every possible size of subset from 1 to n - 1

//         for (int n1 = 1; n1 < n; n1++)
//         {
//             if ((sum * n1) % n == 0)
//             {
//                 int req_sum = (sum * n1) / n;

//                 // check if there is any subset of n1 that has sum of req_sum

//                 if (helper(nums, 0, n, req_sum, n1))
//                     return true;
//             }
//         }

//         return false;
//     }
// };

// NOT working