# # QuickSort



# def partitionArray(arr,left,end):
#     i,j=left,left
#     pivot = len(arr)
    
#     while i < len(arr):
#         if arr[i] < pivot:
#             arr[i],arr[j] = arr[j],arr[i]
#             j+=1
#             i+=1
#         else:
#             i+=1
        
       
#     for i in range(j, len(arr)):
#         if arr[i] == pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             break 

#     return arr

# def quickSort(arr,start,end):
#     if start < end:
#         return
#     pi = partitionArray(arr,start,end)
#     quickSort(arr,start,pi-1)
#     quickSort(arr,pi+1,end)
#     return arr


# arr = [2,5,1,4,3,6,7,9,10,8]
# print(quickSort(arr,0,len(arr)-1))

def partition(arr, start, end):
    pivot = arr[end]  # Choose the last element as the pivot
    i = start - 1  # Pointer for the smaller element region

    for j in range(start, end):
        if arr[j] <= pivot:  # If the current element is smaller or equal to pivot
            i += 1  # Move the boundary pointer
            arr[i], arr[j] = arr[j], arr[i]  # Swap to place the smaller element

    # Place the pivot in the correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1  # Return the pivot index


def quickSort(arr, start, end):
    if start < end:  # Base condition for recursion
        # Partition the array and get the pivot index
        pi = partition(arr, start, end)

        # Recursively sort the sub-arrays
        quickSort(arr, start, pi - 1)  # Sort the left sub-array
        quickSort(arr, pi + 1, end)   # Sort the right sub-array


# Test the implementation
arr = [2, 5, 1, 4, 3, 6, 7, 9, 10, 8]
quickSort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)



