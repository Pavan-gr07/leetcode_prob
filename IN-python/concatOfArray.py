def concatOfArray(arr):
    arr.extend(arr)
    return arr

result = concatOfArray([1,2,1])

print(result)