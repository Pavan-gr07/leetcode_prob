# 21. Binary Array Sorting
# Array
# Sorting
# Paytm


# Given a binary array A[] of size N. The task is to arrange the array in increasing order.

# Note: The binary array contains only 0 and 1.

# Input 1: arr[] = {1, 0, 1, 1, 0}
# Output 1: 0 0 1 1 1
# Explanation 1: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.

# Input 2: arr[] = {1, 0}
# Output 2: 0 1
# Constraints:
# 1 <= A.length <= 105
# 0 <= A[i] <= 1

# def biArrSort(arr):
#     arr.sort()
#     return arr


# for only binarysort
def biArrSort(arr):
    A=len(arr)
    k=0
    for i in range(A):
        if arr[i] == 0:
            temp = arr[k]
            arr[k] = arr[i]
            arr[i] = temp
            k+=1
    return arr

print(biArrSort([1,0,1,1,0]))