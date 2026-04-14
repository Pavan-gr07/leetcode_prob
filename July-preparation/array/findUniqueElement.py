arr =[2, 3, 5, 4, 5, 3, 4]
def uniqueEle(arr):
    ans = 0
    for ele in arr:
        ans ^= ele
    return ans 


print(uniqueEle(arr))