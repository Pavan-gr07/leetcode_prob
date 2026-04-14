# 394. Decode String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square 
# brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra 
# white spaces, square brackets are well-formed, etc. Furthermore, you may 
# assume that the original data does not contain any digits and that digits
#  are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"



def decodeString(str):
    str_stack = []
    num_stack = []

    cur_str = ""
    cur_num = 0
    for s in str:
        if s.isdigit():
            cur_num = cur_num * 10 + int(s)
        elif s == '[':
            num_stack.append(cur_num)
            str_stack.append(cur_str)
            cur_str = ''
            cur_num = 0
        elif s == ']':
            repeat = num_stack.pop()
            prev_str = str_stack.pop()
            cur_str = prev_str + cur_str * repeat
        else:
            cur_str += s
    return cur_str

print(decodeString('3[a]2[bc]')) #aaabcbc
        