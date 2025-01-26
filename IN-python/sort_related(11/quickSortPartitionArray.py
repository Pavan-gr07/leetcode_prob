# base logic of quick sort
def partitionArray(arr):
    i,j= 0,0
    pivot = 5
    
    while i < len(arr):
        if arr[i] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
            i+=1
        else:
            i+=1
        
       
    for i in range(j, len(arr)):
        if arr[i] == pivot:
            arr[i], arr[j] = arr[j], arr[i]
            break 

    return arr


print(partitionArray([2,5,1,4,3,6,7,9,10,8]))