# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104



def mergeIntervals(arr):
    arr.sort(key=lambda x:x[0])

    merged = [arr[0]]
    for ele in arr[1:]:
        last = ele[1]

        if ele[0] <= last[1]:
            last = max(last[1],ele[1])
        else:
            merged.append(ele)

    return merged

print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
