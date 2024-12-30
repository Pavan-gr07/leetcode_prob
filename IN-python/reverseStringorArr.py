# 344. Reverse String
# Solved
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

def reversString(arr):
    # new = []
    # for i in range(len(arr)-1,-1,-1):
    #     new.append(arr[i])
    # return new
    left, right = 0,len(arr)-1

    while left < right:
        arr[left],arr[right] = arr[right] ,arr[left] 
        left += 1
        right -=1
    return arr


print(reversString(["h","e","l","l","o"]))