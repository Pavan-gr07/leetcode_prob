def reverseStringArray(arr):
    left = 0 
    right = len(arr)-1
    temp = arr[left]
    while left <= right:
        arr[right] = temp
        arr[left] = arr[right]
        
        right -= 1
        left += 1
    return arr


print(reverseStringArray(["h","e","l","l","o"]))