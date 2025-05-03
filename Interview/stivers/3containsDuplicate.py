def containsDuplicate(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] +=1
        else:
            dic[arr[i]] = 1

    return any(val > 1 for val in dic.values())

print(containsDuplicate([1,2,3,1]))