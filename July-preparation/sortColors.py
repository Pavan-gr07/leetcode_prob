# 75. Sort Colors
# Solved

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# Bubble Sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if j < len(arr)-1 and arr[j] > arr[j+1]:
                [a,b] = swap1(arr[j] , arr[j+1])
                arr[j] = a
                arr[j+1] = b
    return arr

def swap1(a,b):
    a = a + b
    b = a - b
    a = a - b
    return [a,b]
# TC - O(n^2)
# SC - O(1)


# In Selection Sort, you are not supposed to swap every time you find a smaller element.
# Instead, you should:

# Find the minimum element in the unsorted part.

# Swap once with the current index (i), after the inner loop.
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx] , arr[i]
    return arr

# TC - O(n^2)
# SC - O(1)



def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
    # Function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def quickSort(arr):
    left, right = 0, len(arr) - 1
    mid = len(arr) // 2
    pivot = arr[mid]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
# Try to solve Sort Colors (Leetcode 75) using:

# ✅ Counting sort idea (count 0s, 1s, 2s)

# ✅ Dutch National Flag algorithm (3-pointer O(n), in-place)


# print(swap1(2,3))

# print(quickSort([2,0,2,1,1,0]))
print(insertionSort([85,12,59,45,72,51]))