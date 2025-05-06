def indexSubArrSum(arr,target):
    for i in range(0,len(arr)):
        j = i
        temp = target
        while temp >0 and j<len(arr):
            temp -= arr[j]
            if temp == 0:
                return [i+1,j+1]
            j+=1
    return -1

# TC - O(N ^2)
# SC - O(1)
def indexSubArrSum(arr, target):
    i = 0
    j = 0
    temp = 0

    while j < len(arr):
        temp += arr[j]

        while temp > target and i <= j:
            temp -= arr[i]
            i += 1

        if temp == target:
            return [i + 1, j + 1]

        j += 1

    return -1

print(indexSubArrSum([26 ,3, 28, 7],52))