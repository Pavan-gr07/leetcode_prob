# 15. 3Sum
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.




# import java.util.*;

# public class ThreeSum {
#     public static void main(String[] args) {
#         int[] arr = {-1, 0, 1, 2, -1, -4};

#         Set<List<Integer>> resultSet = new HashSet<>();
#         int n = arr.length;

#         for (int i = 0; i < n; i++) {
#             for (int j = i + 1; j < n; j++) {
#                 for (int k = j + 1; k < n; k++) {
#                     if (arr[i] + arr[j] + arr[k] == 0) {
#                         List<Integer> triplet = Arrays.asList(arr[i], arr[j], arr[k]);
#                         Collections.sort(triplet); // Sort to ensure uniqueness
#                         resultSet.add(triplet);    // HashSet handles duplicates
#                     }
#                 }
#             }
#         }

#         // Convert set to list and print results
#         List<List<Integer>> result = new ArrayList<>(resultSet);
#         for (List<Integer> triplet : result) {
#             System.out.println(triplet);
#         }
#     }
# }

def ThreeSum(arr):

    ans = set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if i!=j and j!=k and i!=k and arr[i]+arr[j]+arr[k] == 0:
                    triple = tuple(sorted([arr[i],arr[j],arr[k]]))
                    ans.add(triple)


    return [list(t) for  t in ans]


# TC- O(N^3)
# SC- O(K)

def ThreeSum1(arr):
    arr.sort()  # Step 1: Sort the array
    result = []

    for i in range(len(arr) - 2):  # Loop through array (fix one element at a time)
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicates for the first element
            continue

        left, right = i + 1, len(arr) - 1  # Initialize two pointers

        while left < right:
            total = arr[i] + arr[left] + arr[right]  # Sum of the triplet

            if total == 0:  # Found a valid triplet
                result.append([i,left,right])

                # Skip duplicates for the second and third elements
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                # Move the pointers after finding a valid triplet
                left += 1
                right -= 1

            elif total < 0:  # If sum is less than 0, move left pointer to the right
                left += 1
            else:  # If sum is greater than 0, move right pointer to the left
                right -= 1

    return result



# TC- O(N^2)
# SC- O(K)
print(ThreeSum1([0, -1, 2 ,-3 ,1]))
