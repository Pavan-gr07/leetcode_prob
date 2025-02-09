# Find all pairs with a given sum in two unsorted arrays
# Last Updated : 15 Sep, 2024
# Given two unsorted arrays of distinct elements, the task is to find all pairs from both arrays whose sum is equal to a given value X.

# Examples: 

# Input: arr1[] = {-1, -2, 4, -6, 5, 7}, arr2[] = {6, 3, 4, 0} , x = 8
# Output: 4 4 5 3


# Input: arr1[] = {1, 2, 4, 5, 7}, arr2[] = {5, 6, 3, 4, 8}, x = 9
# Output: 1 8 4 5 5 4



def allPairs(arr1,arr2,target):
    ans = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j] == target:
                ans.append([arr1[i],arr2[j]])
    ans.sort()
    return ans

def allPairsEfficient(m,n,target):
    ans = []
    m.sort()
    n.sort()
    left,right = 0,len(n)-1
    sum = 0
    while left < len(m) and right >= 0:
        sum = m[left]+n[right]
        if sum == target:
            ans.append([m[left],n[right]])
            left+=1
            right -=1
        else:
            if sum < target:
                left+=1
            else:
                right -=1

    return ans

print(allPairsEfficient([1, 2, 4, 5, 7],[5, 6, 3, 4, 8],9))