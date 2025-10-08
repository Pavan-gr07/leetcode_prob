# Next Smaller Element
# Difficulty: MediumAccuracy: 36.26%Submissions: 203K+Points: 4Average Time: 20m
# You are given an integer array arr[ ]. For every element in the array, your task is to determine its Next Smaller Element (NSE).


# The Next Smaller Element (NSE) of an element x is the first element that appears to the right of x in the array and is strictly smaller than x.

# If no such element exists, assign -1 as the NSE for that position.
# Examples:

# Input: arr[] = [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]
# Explanation: 
# The first element smaller than 4 having index > 0 is 2.
# The first element smaller than 8 having index > 1 is 5.
# The first element smaller than 5 having index > 2 is 2.
# There are no elements smaller than 4 having index > 3.
# There are no elements smaller than 4 having index > 4.
# Input: arr[] = [13, 7, 6, 12]
# Output: [7, 6, -1, -1]
# Explanation:
# The first element smaller than 13 having index > 0 is 7.
# The first element smaller than 7 having index > 1 is 6.
# There are no elements smaller than 6 having index > 2.
# There are no elements smaller than 12 having index > 3.

# Input: arr[] = [4, 1]
# Output: [1, -1]
# Explanation: 4 will be updated to 1 and 1 will be updated to -1
# 
# 

def nextSmallerElement(arr):
    stack = []
    result = []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] >= arr[i]: # increasing monotonic stack always stores bigger element at the top pop all smaller element 
            stack.pop()
        
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(arr[i])
    
    return result[::-1]


print(nextSmallerElement(([4, 8, 5, 2, 25])))