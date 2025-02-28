# Extra Parentheses Around an Expression: ((a+b)) → The outermost brackets are unnecessary.
# Unnecessary Parentheses Around a Single Element: (a)+b → The parentheses around a are not needed.

# Note: Expression may contain ‘+‘, ‘*‘, ‘–‘ and ‘/‘ operators. Given expression is valid and there are no white spaces present.

# Examples: 

# Input: s = “((a+b))”
# Output: True
# Explanation: ((a+b)) can reduced to (a+b), this Redundant


# Input: s = “(a+(b)/c)”
# Output: False
# Explanation: (a+(b)/c) can reduced to (a+b/c) because b is surrounded by () which is redundant.


# Approach: Using Stack

def redundant(str):
    ans =[]
    for ele in str:
        if ele ==')':
            top = ans[-1]
            ans.pop()
            flag =True
            while top != "(":
                if top in {"+","-","*","/"}:
                    flag = False
                top =ans[-1]
                ans.pop()

            if flag:
                return True
        else:
            ans.append(ele)
            
    return False

print(redundant("((a+b))"))