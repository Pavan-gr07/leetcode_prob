# Write a function that reverses a string. The input string is given as an array of characters s.

# Input 1: s = "bosscoder"
# Output 1: redocssob
# Explanation 1: Reverse of "bosscoder" is "redocssob"
# Input 2: s="abc"
# Output 2: cba


def reverseString(s):
    
    left,right =0,len(s)-1

    while  left< right:
        s[left] ,s[right] = s[right],s[left]
        left +=1
        right -=1
    return s



print(reverseString(["h","e","l","l","o"]))