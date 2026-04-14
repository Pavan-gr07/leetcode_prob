def removeElement(arr,val):
    start = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[start] = arr[i]
            start += 1
    return arr,start

print(removeElement([0,1,2,2,3,0,4,2],2))
