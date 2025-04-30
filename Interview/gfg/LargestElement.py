def largestElement(arr):
    maxEle = 0
    for i in range(len(arr)):
        if arr[i] > maxEle:
            maxEle = arr[i]
    return maxEle

print(largestElement([3, 3, 6, 1]))