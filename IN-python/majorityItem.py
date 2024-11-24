def majorityItem(arr):
    newArr = {}
    for x in arr:
        if x in newArr:
            newArr[x] += 1
        else:
            newArr[x] = 1
    large =0
    itemValue = None
    for item,value in newArr.items():
        # print(value)
        if value > large:
            large = value
            itemValue = item
        
    return itemValue


result = majorityItem([2,2,1,1,1,2,2])
print(result)


# from collections import Counter

# def majorityItem(arr):
#     count = Counter(arr)
#     print(count)
#     return max(count, key=count.get)

# result = majorityItem([2, 2, 1, 1, 1, 2, 2])
# print(result)
