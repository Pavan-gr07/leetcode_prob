# Given a string, the task is to reverse the order of the words in the given string.

# Input 1: s = “bosscoder quiz practice code”
# Output 1: “code practice quiz bosscoder”
# Explanation 1: The last word comes first, the second last comes second first and so on.

# Input 2: s = “i love programming very much”
# Output 2: “much very programming love i”
# Constraints:
# 1 <= s.length <= 105


def reverseWordsInStrings(str):
    temp = []
    str1 = ''
    ans =''

    # here two filter for space before and after the string
    for ele in str:
        if ele !=' ':
            str1 += ele
        else:
            temp.append(str1)
            str1=""
    temp.append(str1)      

    while temp:
        top_element = temp[-1]# Access the top element (last element in the list)
        if top_element !="":
            ans += top_element + ' '
        temp.pop()
    return ans.strip()+"---"



print(reverseWordsInStrings("the sky is blue" ))
