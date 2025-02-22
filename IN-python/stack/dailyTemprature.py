# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]



def temperatures(arr):
    ans = [0]*len(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                ans[i] = j - i
                break
    return ans

print(temperatures([73,74,75,71,69,72,76,73]))