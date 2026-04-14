# You are given an array of integers arr of size n and an integer target.

# Write a recursive function to find the index of the first occurrence of target in the array.

# If the element is found, return its index (0-based).

# If the element is not present, return -1.

# You are not allowed to use loops.



def firstOccurence(arr,index,target):

    if len(arr) == index :
        return -1

    if arr[index] == target:
        return index
    
    return firstOccurence(arr,index+1,target)

# TC - O(n)
# SC - O(n)

# print(firstOccurence([2, 2, 2, 2],0,2))



def lastOccurance(arr,index,target):
    if index <=0:
        return -1
    
    if arr[index] == target:
        return index
    
    return lastOccurance(arr,index-1,target)

def lastOccurance1(arr, index, target):
    if index == len(arr):
        return -1

    res = lastOccurance1(arr, index + 1, target)

    if res != -1:
        return res

    if arr[index] == target:
        return index

    return -1

def countOcc(arr, index, target,ans):
    if index == len(arr):
        return -1

    countOcc(arr, index + 1, target,ans)

    if arr[index] == target:
        ans.append(index)

ans = []
countOcc([2,2,2,2],0,2,ans)

print(ans)