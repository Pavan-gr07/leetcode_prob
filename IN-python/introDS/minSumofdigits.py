# Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of the given array must be used to form the two numbers.

# Any combination of digits may be used to form the two numbers to be summed. Leading zeroes are permitted.

# If forming two numbers is impossible (i.e. when n==0) then the "sum" is the value of the only number that can be formed.

# Input 1: arr[] = {6, 8, 4, 5, 2, 3}
# Output 1: 604
# Explanation 1: The minimum sum is formed by numbers 358 and 246

# Input 2: arr[] = {5, 3, 0, 7, 4}
# Output 2: 82
# Constraints:
# 1 <= arr.length <= 35
# 0 <= arr[i] <= 9




def minSum(digits):
    res=0
    digits = sorted(digits,reverse=True)
    n = len(digits)    
    res = 0
    even_iteration = False
    position = 0
    for i in range(n):
        res += int(digits[i])*(10**position)
        if even_iteration:
            position += 1
            even_iteration = False
        else:
            even_iteration = True
    return res




print(minSum([5, 3, 0, 7, 4]))



# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

 

# Example 1:

# Input: num = 2932
# Output: 52
# Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
# The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
# Example 2:

# Input: num = 4009
# Output: 13
# Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
# The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.

# class Solution(object):
#     def minimumSum(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         a,b,c,d = sorted(str(num))
#         return int(a+c)+int(b+d)
        



        # ********************************************************************************************** 


#         def find_min_sum(arr):
#     # Step 1: Sort the array in ascending order
#     arr.sort()

#     # Step 2: Initialize two numbers as strings
#     num1 = ""
#     num2 = ""

#     # Step 3: Distribute the digits alternately between the two numbers
#     for i, digit in enumerate(arr):
#         if i % 2 == 0:
#             num1 += str(digit)
#         else:
#             num2 += str(digit)

#     # Step 4: Convert the numbers to integers and calculate their sum
#     result = int(num1) + int(num2)

#     return result

# # Test Cases
# print(find_min_sum([6, 8, 4, 5, 2, 3]))  # Output: 604
# print(find_min_sum([5, 3, 0, 7, 4]))     # Output: 82
# print(find_min_sum([1, 2, 3, 4, 5]))     # Output: 46
# print(find_min_sum([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # Output: 975
