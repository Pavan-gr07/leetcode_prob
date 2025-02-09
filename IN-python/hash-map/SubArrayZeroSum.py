def subArrayZeroSum(arr):
    sum =0
    check = {}
    for i in range(len(arr)):
        sum += arr[i]
        if sum ==0:
            return True
        else:
            if sum in check:
                return True
            else:
                check[sum] = i

    return False

print(subArrayZeroSum([10,15,1,2]))