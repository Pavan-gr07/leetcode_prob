# 47. Check if two arrays are equal or not
# Array
# Microsoft
# GoldmanSachs


# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
    
#     Input 1: A[] = {1,2,5,4,0} , B[] = {2,4,5,0,1}
# Output 1: true
# Explanation 1: Both the array can be rearranged to {0,1,2,4,5}

# Input 2: A[] = {1,2,5} , B[] = {2,4,15}
# Output 2: false
# Constraints:
# 1 <= A.length, B.length <= 105
# 1<= A[i], B[i] <= 106



def checkArrayEq(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq1 = {}
    freq2 = {}
    for i in arr1:
        freq1[i] = freq1.get(i,0)+1
    for j in arr2:
        freq2 [j] = freq2.get(j,0)+1

    return freq1==freq2


print(checkArrayEq([1,2,5],[2,4,15]))