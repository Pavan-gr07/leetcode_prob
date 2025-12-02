# 22. Generate Parentheses
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


def generateParathesis(n):
    result = []

    def backtrack(curr,open_count,close_count):

        if len(curr) == 2*n:
            result.append(curr)
            return 
        
        if open_count < n:
            backtrack(curr+"(",open_count+1,close_count)

        if close_count < open_count:
            backtrack(curr+")",open_count,close_count+1)

    backtrack("",0,0)
    return result
    
print(generateParathesis(3))