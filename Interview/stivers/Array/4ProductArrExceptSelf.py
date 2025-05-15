def productArrExceptSelf(arr):
    ans =[]
    for i in range(len(arr)):
        pro_val = 1
        for j in range(len(arr)):
            if j != i:
                pro_val *= arr[j]
        ans.append(pro_val)

    return ans

# TC - O(N^2)
# SC - O(N)

def productArrExceptSelf1(arr):
    ans =[]
    all = 1
    for ele in arr:
        all *= ele

    for i in range(len(arr)):
        ans.append(all//arr[i])
    return ans

# TC - O(N+N) - O(N)
# SC - O(N)

def productArrExceptSelf2(arr):
    n = len(arr)
    res = [1] * n

    # First pass: left product
    left = 1
    for i in range(n):
        res[i] = left
        left *= arr[i]

    # Second pass: right product
    right = 1
    for i in reversed(range(n)):
        res[i] *= right
        right *= arr[i]

    return res





print(productArrExceptSelf2([1,2,3,4]))
