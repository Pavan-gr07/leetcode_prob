# 315. Count of Smaller Numbers After Self
# Hard
# Topics
# Companies
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

# Example 1:

# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Example 2:

# Input: nums = [-1]
# Output: [0]
# Example 3:

# Input: nums = [-1,-1]
# Output: [0,0]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

#  this TC - O(n2) --leetcode it won't work 
#  another approach is using merge sort
def countSmall(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count += 1
        ans.append(count)
    return ans

print(countSmall([5,2,6,1]))




# Certainly! Here's a step-by-step explanation of how the **optimized algorithm** works to count smaller elements to the right using a merge sort-based approach:

# ---

# ### **Problem Recap**
# We want to count, for each element in the array, how many elements to its right are smaller than it. For example:

# Input: `[5, 2, 6, 1]`  
# Output: `[2, 1, 1, 0]`  
# - For `5`, the smaller elements to the right are `[2, 1]` → `2`.
# - For `2`, the smaller element to the right is `[1]` → `1`.
# - For `6`, the smaller element to the right is `[1]` → `1`.
# - For `1`, there are no smaller elements to the right → `0`.

# ---

# ### **Key Idea**
# Instead of comparing every element pair (which takes \(O(n^2)\)), we leverage the **merge sort** process. During the merge step of merge sort:
# 1. The left and right halves are already sorted.
# 2. For each element in the left half, we can count how many elements in the right half are smaller and are placed before it during the merge.

# ---

# ### **Steps in Detail**

# #### **1. Track Indices**
# We use an `indices` array to track the original positions of elements in the array. This ensures that the results are stored correctly for each element.

# Example:  
# For the array `[5, 2, 6, 1]`, the indices array starts as `[0, 1, 2, 3]`.  

# #### **2. Divide Step (Recursive)**
# Split the array into two halves recursively until each subarray contains a single element. This is the standard divide step of merge sort.

# Example:
# - Split `[5, 2, 6, 1]` → `[5, 2]` and `[6, 1]`
# - Split `[5, 2]` → `[5]` and `[2]`
# - Split `[6, 1]` → `[6]` and `[1]`

# ---

# #### **3. Merge Step**
# When merging two sorted halves, do the following:

# 1. Compare elements from the left and right halves.
# 2. If an element from the **right half** is smaller, it means it is smaller than all remaining elements in the **left half** (because both halves are sorted). Increment a count for those left-half elements.
# 3. Append elements into a temporary array to rebuild the sorted array.
# 4. Update the `result` array for elements in the left half.

# **Example: Merging `[5]` and `[2]`**
# - Compare `5` and `2`. Since `2 < 5`, we:
#   - Append `2` to the merged array.
#   - Increment the count for `5` by `1` (as `2` is smaller than `5`).
# - Final merged array: `[2, 5]`
# - `result` becomes: `[1, 0, 0, 0]` (updated count for `5`).

# ---

# #### **4. Maintain Order Using Indices**
# The `indices` array ensures that the counts are updated for the correct original positions of elements, even as we split and merge.

# **Example: Indices Transformation**
# - Start with `indices = [0, 1, 2, 3]`.
# - After merging `[5]` and `[2]`, the indices become `[1, 0]` (corresponding to `[2, 5]`).

# ---

# #### **5. Combine Results**
# Continue merging the subarrays, updating the `result` array at each step.

# **Example: Merging `[2, 5]` and `[1, 6]`**
# - Compare elements:
#   - `2 > 1`: Add `1` to the merged array. Increment the count for `2` and `5`.
#   - `5 > 1`: Add `5` to the merged array. Increment the count for `5`.
#   - Append remaining elements in order.
# - Final merged array: `[1, 2, 5, 6]`
# - `result` becomes: `[2, 1, 1, 0]`.

# ---

# ### **Code Walkthrough**

# Here's the code again with comments:

# ```python
# def count_smaller_elements(arr):
#     n = len(arr)
#     result = [0] * n  # Initialize result array with zeros
#     indices = list(range(n))  # Track original indices

#     # Recursive function for merge sort
#     def merge_sort(start, end):
#         if end - start <= 1:  # Base case: single element
#             return
        
#         mid = (start + end) // 2
#         merge_sort(start, mid)  # Sort left half
#         merge_sort(mid, end)    # Sort right half

#         # Merge step
#         temp = []
#         left, right = start, mid
#         right_count = 0  # Count of smaller elements in right half

#         while left < mid and right < end:
#             if arr[indices[right]] < arr[indices[left]]:
#                 temp.append(indices[right])
#                 right_count += 1
#                 right += 1
#             else:
#                 temp.append(indices[left])
#                 result[indices[left]] += right_count
#                 left += 1

#         while left < mid:  # Append remaining left elements
#             temp.append(indices[left])
#             result[indices[left]] += right_count
#             left += 1

#         while right < end:  # Append remaining right elements
#             temp.append(indices[right])
#             right += 1

#         indices[start:end] = temp  # Update indices to reflect sorted order

#     merge_sort(0, n)  # Start merge sort
#     return result  # Return the final counts
# ```

# ---

# ### **Final Output**
# For the input array `[5, 2, 6, 1]`, the algorithm produces the result:

# - Final sorted array: `[1, 2, 5, 6]`
# - Result array: `[2, 1, 1, 0]`

# ---

# ### **Time Complexity**
# 1. **Divide Step**: \(O(\log n)\) splits.
# 2. **Merge Step**: \(O(n)\) operations per merge.
# 3. Total: \(O(n \log n)\).

# This is significantly faster than the \(O(n^2)\) brute-force approach for large arrays.