def secondLargest(arr):
    max_val = float('-inf')
    sec_val = float('-inf')
    for i in range(len(arr)):
       
        if arr[i] > max_val:
            sec_val = max_val
            max_val = arr[i]
        elif arr[i] != max_val and arr[i] > sec_val:
            sec_val = arr[i] 


    return sec_val


print(secondLargest([10,5,10]))