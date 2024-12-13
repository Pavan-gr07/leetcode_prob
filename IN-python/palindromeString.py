# Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. The function should return `True` if the string is a palindrome and `False` otherwise.

# Input 1: “abcba”
# Output 1: true
# Explanation 1: The above string remains the same on reading from both ends.

# Input 2: “abcaa”
# Output 2: false
# Constraints:
# 1 <= str.length <= 105



def palindrome(str):
    original = str
    temp = ""
    print(len(str))
    for i in range(len(str)-1,-1,-1):
        temp+=str[i]

    print(temp)
    if original == temp:
        return True
    else:
        return False



print(palindrome("abcba"))