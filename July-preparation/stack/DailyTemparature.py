def dailyTemparature(num2): 
    stack = [] 
    length = len(num2) 
    ans = [0]*len(num2) 
    for i in range(length-1,-1,-1):
        while stack and num2[stack[-1]] <= num2[i]: 
             stack.pop()
             
        if stack: 
            ans[i] = stack[-1] - i
        else: 
            ans[i] = 0

        stack.append(i)
        

    return ans
    
print(dailyTemparature([73,74,75,71,69,72,76,73]))