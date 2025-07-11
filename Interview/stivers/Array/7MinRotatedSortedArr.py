
# Blogs

# User
# Toggle Sidebar

# DSA Sheet

# DSA Playlist
# Folder IconArray Series
# Folder IconBinary Search Series
# Folder IconString Series
# Folder IconLinkedList Series
# Folder IconRecursion Series
# Folder IconStack and Queue Series
# Folder IconTree Series
# Folder IconGraph Series
# Folder IconDP Series

# Core Subjects
# Folder IconDBMS
# Folder IconOperating System
# Folder IconComputer Networks

# Others
# Use code "PAYDAY" to get a 35 % discount
# Last sale before V3 launch. 🚀
# Click Here
# TUF
# Unlock personalized learning and exclusive roadmaps.
# Explore Plans
# Premium Icon
# Get Plus
# Minimum in Rotated Sorted Array

# Mark as Completed

# 123


# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

# Pre-requisites: Search in Rotated Sorted Array I,  Search in Rotated Sorted Array II & Binary Search algorithm

# Examples

# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3]
# Result: 0
# Explanation: Here, the element 0 is the minimum element in the array.

# Example 2:
# Input Format: arr = [3,4,5,1,2]
# Result: 1
# Explanation: Here, the element 1 is the minimum element in the array.


def minRotaedSortArray(arr):
    #complete the function here
    mini = arr[0]
    for ele in arr:
        if ele < mini:
            mini = ele
    return mini

print(minRotaedSortArray( [5, 6, 1, 2, 3, 4]))