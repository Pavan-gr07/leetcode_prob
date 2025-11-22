# 541. Reverse String II
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

def reverseString2(s,k):
    new_s = [0]*len(s)
    for i in range(len(s)):
        new_s[i] = s[i]

    for i in range(0,len(new_s),2*k):
        left = i
        right = min(i + k - 1, len(s) - 1)


        while left < right:
            new_s[left],new_s[right] = new_s[right],new_s[left]

            left +=1
            right -= 1
            
    return "".join(new_s)

print(reverseString2("abcdefg",2))