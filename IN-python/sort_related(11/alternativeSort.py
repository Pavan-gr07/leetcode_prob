# 12. Alternative Sorting
# Array
# Sorting
# Google
# Jp Morgan
# Apple


# Given an array arr[] of N distinct integers, output the array in such a way that the first element is first maximum and the second element is the first minimum, and so on.

# Input 1: N = 7, arr[] = {7, 1, 2, 3, 4, 5, 6}
# Output 1: 7 1 6 2 5 3 4
# Explanation 1: The first element is first maximum and second element is first minimum and so on.

# Input 2: N = 8, arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
# Output 2: 9 1 8 2 7 3 6 4
# Constraints:
# 1 <= A.length <= 105
# 1 <= A[i] <= 106



def alternativeSort(arr):
    ans = [0]*7
    arr.sort()
    set=True
    k= 0
    l=0
    for i in range(len(arr)):
        if set == True:
            ans[i] = arr[len(arr)-1-l]
            set=False
            l+=1
        else:
            ans[i] = arr[k]
            k+=1
            set=True
    return ans
print(alternativeSort([7,1,2,3,4,5,6]))