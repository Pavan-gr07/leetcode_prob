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



def longestValidParentheses( s):
       
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

print(longestValidParentheses("(()"))