def TwoSum(arr,target):
    look = {}
    for i in range(len(arr)):
        value = target -arr[i]
        if value in look:
            return [look[value],i]
        look[arr[i]] = i
    return [-1,-1]

print(TwoSum([2,7,11,15],9))
