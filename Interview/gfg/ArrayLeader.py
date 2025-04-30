def arrayLeader(arr):
    ans =[]
    def isAnyGreater(i):
        j = i+1
        while j < len(arr):
            if arr[j] > arr[i]:
                return True
            j+=1
        return False    
    for i in range(len(arr)):
        if(not isAnyGreater(i)):
            ans.append(arr[i])
    return ans
def arrayLeader1(arr):
    ans =[]
    max_val = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i] >= max_val:
            ans.append(arr[i])
            max_val = arr[i]
    return ans[::-1]

print(arrayLeader1( [30, 10, 10, 5]))