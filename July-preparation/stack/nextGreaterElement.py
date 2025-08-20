def nextGreaterElement(num1,num2): 
    stack = [] 
    length = len(num2) 
    ans = [] 
    freq = {} 
    for i in range(length-1,-1,-1):
        while stack and stack[-1] < num2[i]: 
             stack.pop()
             
        if stack: 
            freq[num2[i]] = stack[-1] 
        else: 
            freq[num2[i]] = -1 
        stack.append(num2[i])
        for ele in num1:
            ans.append(freq[ele])

        return ans