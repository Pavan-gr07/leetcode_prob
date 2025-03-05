# 239. Sliding Window Maximum
# Hard
# Topics
# Companies
# Hint
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

#  Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


def slidingWindowMax(arr,k):
    ans =[]
    temp = arr[:k]
    for i in range(len(arr)):
        max_ele = -1
        for ele in temp:
            if ele > max_ele:
                max_ele = ele
        ans.append(max_ele)
        temp = arr[i+1:k+i+1]
        if len(temp) <k:
            return ans

# TC - O(N*K)
# SC - O(n)

from collections import deque
def slidingWindowMax1(arr,k):
    dq = deque()
    ans = []
    
    for i in range(len(arr)):
        # Remove elements that are out of this window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove elements from the back if they are smaller than arr[i]
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        # Add the current element index
        dq.append(i)
        
        # Start adding max elements to ans once we have at least k elements processed
        if i >= k - 1:
            ans.append(arr[dq[0]])  # Front of the deque is the max of this window
    return ans

def slidingWindowMax2(arr,k):
    start = 0
    end = 0
    que = deque([])
    ans = []
    while end < len(arr):
        if que and arr[que[-1]] < arr[end]:
            que.pop()
        que.append(end)
        if que[0] < start:
            que.popleft()
        if end - start + 1 >= k:
            ans.append(arr[que[0]])
            start += 1
        end += 1
    return ans



print(slidingWindowMax2([6,5,4,3],2))