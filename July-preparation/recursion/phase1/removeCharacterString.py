# def removeChracter():
#     Great! This is the **perfect next recursion problem** 🔥
# Here are clear **problem statements + examples** so you can solve it confidently.

# ---

# # 📌 Problem: Remove a Character From a String (Using Recursion)

# ### **Problem Statement**

# You are given a string `s` and a character `ch`.
# Write a **recursive function** that returns a **new string** after removing **all occurrences** of `ch` from `s`.

# * Do **not** use loops.
# * Do **not** modify the original string directly.

# ---

# # 📘 Examples

# ### Example 1

# ```
# Input:
# s = "banana"
# ch = 'a'

# Output:
# "bnn"
# ```

# ### Example 2

# ```
# Input:
# s = "hello world"
# ch = 'l'

# Output:
# "heo word"
# ```

# ### Example 3

# ```
# Input:
# s = "aaaaa"
# ch = 'a'

# Output:
# ""
# ```

# ### Example 4

# ```
# Input:
# s = "abcdef"
# ch = 'x'

# Output:
# "abcdef"
# ```

# ### Example 5

# ```
# Input:
# s = "recursion"
# ch = 'r'

# Output:
# "ecusion"
# ```

# ---

# # 💡 Hints (Don’t look unless needed)

# ### Hint 1

# Check the **first character** of the string.

# ### Hint 2

# If it's equal to `ch`, **skip it**, otherwise **add it** to the answer.

# ### Hint 3

# Recursively call the function on `s[1:]`.

# ---

# # 🎯 Function signature

# ```python
# def removeChar(s, ch):
#     pass
# ```

# ---

# # 🚀 You Solve Now

# Send your code — I’ll review and improve it if needed.

def removeChar(s, ch):
    if s == "":
        return ''
    
    smallAns = removeChar(s[1:],"a")
    if s[0] == ch:
        return smallAns
    else:
        return s[0] + smallAns
    


# def reverString(s):
#     if s=="":
#         return ""
    
#     return  reverString(s[1:])+ s[0] 

print(removeChar("banana","a"))