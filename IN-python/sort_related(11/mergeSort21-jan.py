# 148. Sort List
# Medium
# Topics
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105


def merge(a,b):
    res = [0]*(len(a)+len(b))
    i,j,k, = 0,0 ,0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            res[k] = a[i]
            i+=1
        else: 
            res[k] = b[j]
            j+=1
        k+=1
    while i<len(a):   #this steps is for remaining elements in array a
        res[k] = a[i]
        i+=1
        k+=1
    while j<len(b): #this steps is for remaining elements in array b
        res[k] = b[j]
        j+=1
        k+=1
    return res



def mergeSort(arr,start,end):
    mid = (start+end)//2
    if start == end:
        return [arr[start]]

    firstHalf = mergeSort(arr,start,mid)
    secondHalf = mergeSort(arr,mid+1,end)
    return merge(firstHalf,secondHalf)

arr=[5,1,1,2,0,0]
print(mergeSort(arr,0,len(arr)-1))