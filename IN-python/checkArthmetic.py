def checkArthmetic(arr):

    arr.sort()
    print(arr)
    diff = arr[1] - arr[0]
    for i in range(2,len(arr)-1):
        if arr[i]-arr[i-1] != diff:
            return False

    return True


print(checkArthmetic([0,12,4,8]))   
