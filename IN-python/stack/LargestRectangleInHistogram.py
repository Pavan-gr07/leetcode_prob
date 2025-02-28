# 84. Largest Rectangle in Histogram
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.


def largestHistogram(arr):
    stack =[]
    max_area = 0
    arr.append(0)
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            l = arr[stack.pop()]
            w = i if not stack else i -stack[-1] -1
            max_area = max(max_area,l*w)
        stack.append(i)
    return max_area

print(largestHistogram([2,4]))