# 32. Longest Valid Parentheses
# Hard
# Topics
# Companies
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring
# .

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0



def longestValidParentheses2( s):
       
        count = 0
        stack =[-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else :
                stack.pop()
                if stack:
                    count = max(count,i-stack[-1])
                else:
                    stack.append(i)
        return count
# TC - O(N)
# Sc - O(1)


def longestValidParentheses( s):
    open,close,ans1,ans2 =0,0,0,0
    for i in range(len(s)):
        if s[i] == '(':
            open+=1
        else:
            close+=1
        if open == close:
            ans1 =max(ans1,open+close) 
        elif close> open:
            open =0
            close = 0
        
    open2, close2 = 0, 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == '(':
            open2+=1
        else:
            close2+=1
        if open2 == close2:
            ans2 =max(ans2,open2+close2) 
        elif open2>close2:
            open2 =0
            close2 =0
    return max(ans1,ans2)

# TC - O(2(N))
# Sc - O(1)
print(longestValidParentheses("(()"))
