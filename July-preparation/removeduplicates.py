def removeDuplicates(arr):
    dict = {}
    ans = ["_"]*len(arr)
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
    for i,ele in enumerate(dict.keys()):
        ans[i] = ele
    return len(dict),ans


# TC - O(n)
# SC - O(n)

# Try to implement using IN- place SC - O(1)


def removeDuplicatedInplace(arr):
    left = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[left - 1]:
            arr[left] = arr[i]
            left += 1
    return arr

print(removeDuplicatedInplace([0,0,1,1,1,2,2,3,3,4]))