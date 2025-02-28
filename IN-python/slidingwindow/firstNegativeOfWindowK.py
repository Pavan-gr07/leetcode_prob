# First negative in every window of size k
# Difficulty: MediumAccuracy: 48.61%Submissions: 177K+Points: 4Average Time: 15m
# Given an array arr[]  and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

# Note: If a window does not contain a negative integer, then return 0 for that window.

# Examples:

# Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
# Output: [-8, 0, -6, -6]
# Explanation:
# Window {-8, 2}: First negative integer is -8.
# Window {2, 3}: No negative integers, output is 0.
# Window {3, -6}: First negative integer is -6.
# Window {-6, 10}: First negative integer is -6.
# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
# Output: [-1, -1, -7, -15, -15, 0] 
# Explanation:
# Window {12, -1, -7}: First negative integer is -1.
# Window {-1, -7, 8}: First negative integer is -1.
# Window {-7, 8, -15}: First negative integer is -7.
# Window {8, -15, 30}: First negative integer is -15.
# Window {-15, 30, 16}: First negative integer is -15.
# Window {30, 16, 28}: No negative integers, output is 0.


from collections import deque
def firstNegativeWindowK(arr,k):
    start,end = 0,0
    que =deque()
    ans = []
    while end < len(arr):
        if arr[end] < 0:
            que.append(arr[end])
            
        if end - start + 1 < k:
            end +=1
        elif end - start + 1 == k:
            if que:
                ans.append(que[0])
                if arr[start] == que[0]:
                    que.popleft()   
            else:
                ans.append(0)
         
            start += 1
            end += 1
         
    return ans

print(firstNegativeWindowK([12, -1, -7, 8, -15, 30, 16, 28],3))