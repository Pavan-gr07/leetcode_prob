# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# 88******************* Approach ***************************
#  length * breadth
# min(height[left],height[right]) * (right - left)
# ans =0
# ans = max(ans,area)

def containMostWater1(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            area = min(arr[i],arr[j]) * (j - i)
            ans = max(ans,area)
    return ans

# TC - O(n2)
# SC - O(1)

def containMostWater(arr):
    ans = 0
    left, right = 0,len(arr)-1
    while left < right:
        area = min(arr[left],arr[right]) * (right - left)
        ans = max(ans,area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -=1 
    return ans
# TC - O(n)
# SC - O(1)

print(containMostWater1( [1,8,6,2,5,4,8,3,7]))