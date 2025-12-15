# Most Frequent Element in an Array
# Difficulty: EasyAccuracy: 46.55%Submissions: 11K+Points: 2
# You are given an integer array arr[]. You need to return the element which occurs maximum times in arr[].
# Note: If multiple such elements exists return the maximum element.

# Example: 

# Input: arr[] = [1, 2, 2, 2, 4, 1]
# Output: 2
# Explanation: 2 is most frequent element of this array with 3 occurrences.
# Input: arr[] = [1, -5, 8, 1]
# Output: 1
# Explanation: 1 is most frequent element of this array with 2 occurrences.
# Input: arr[] = [3, 0, 0, 3, 8]
# Output: 3
# Explanation: 0 and 3 are two most frequent elements of this array. 3 is the maximum one.


def maxFreqele(arr):
    freq = {}

    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] = freq[arr[i]] +1
        else:
            freq[arr[i]] = 1
    max_freq = 0
    res =  float('-inf')
    for key,value in freq.items():
        if value > max_freq or( value == max_freq and key > res ):
            max_freq = value
            res = key

    return res

print(maxFreqele([1, -2, 3, 3, -1, -2, -1, -2, 2, 5]))