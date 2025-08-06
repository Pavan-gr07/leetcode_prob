def validParthesis(s):
    stack = []
    bracket = { "}" : "{","]" : "[" ,")":"("}
    if len(s) <= 1:
        return False
    for ele in s:
        if ele in bracket.values():
            stack.append(ele)
        elif ele in bracket:
            if stack and stack[-1] == bracket[ele]:
                stack.pop()
            else:
                return False
            
        if len(stack) > 0:
            return False
        else:
            return True
    

print(validParthesis("(()"))