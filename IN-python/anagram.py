# 13. Anagram String
# String
# Google
# Jp Morgan
# Apple


# Check whether two Strings are anagram of each other.
# Note : An anagram of a string is another string that contains the same characters, only the order of characters can be different.

# Input 1: str1 = “listen” str2 = “silent”
# Output 1: true
# Explanation 1: All characters of “listen” and “silent” are the same.

# dict = {
#     l:1,
#     i:1,
#     s:1,
#     t:1,
#     e:1,
#     n:1
# }




# Input 2: str1 = “gram” str2 = “arm”
# Output 2: false
# Constraints:
# 1 <= str1.length, str2.length <= 105

def anagram(str1,str2):
    if(len(str1) != len(str2)):
        return False

    dict = {}
    for str in str1:
        if str in dict:
           dict[str]+=1
        else:
            dict[str] = 1

    for str in str2:
        if str in dict:
            dict[str] -= 1
        else:
            return False

    for count in dict.values():
        if count != 0:
            return False
    return True



print(anagram('listen','silent'))