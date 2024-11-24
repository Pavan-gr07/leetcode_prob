def singleNumber(arr):
    newArr = {}
    for x in arr:
        if x in newArr:
            newArr[x] += 1
        else:
            newArr[x] = 1

            
    for key,value in newArr.items():
        if value==1:
            return key
       


result = singleNumber([4,1,2,1,2])

print(result)