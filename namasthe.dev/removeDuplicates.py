arr = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(arr):
    start = 1
    for i in range(1,len(arr)):
        if  arr[i] != arr[start - 1]:
            arr[start] = arr[i]
            start += 1
    return arr,start
print(removeDuplicates(arr))