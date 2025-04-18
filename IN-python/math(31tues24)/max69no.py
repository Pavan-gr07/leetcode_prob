# 1323. Maximum 69 Number
# Easy
# Topics
# Companies
# Hint
# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
 

# Constraints:

# 1 <= num <= 104
# num consists of only 6 and 9 digits.


# note:
# string is immutable


def max69No(num):
    max = num
    strNum = list(str(num))
    for i in range(len(strNum)):
        original_digit = strNum[i]
        if strNum[i] == '6':
            strNum[i] = '9'
        else:
            strNum[i] = '6'
           
        newNum = int("".join(strNum))

        if newNum>max:
                max = newNum
        
        strNum[i] = original_digit

    return max

# optimize
def max69No1(num):
    strNum = list(str(num))
    for i in range(len(strNum)):
        if strNum[i] == '6':
            strNum[i] = '9'
            break
       

    return int("".join(strNum))


print(max69No1(9669))