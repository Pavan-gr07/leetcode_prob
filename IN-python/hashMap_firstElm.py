# Given an array of N integers. Find the first element that occurs at least K number of times.
#  If the answer is not present in the array, return -1.

# Input 1: N = 7, K = 2, A[] = {1, 7, 4, 3, 4, 8, 7}
# Output 1: 4
# Explanation 1: Both 7 and 4 occur 2 times. But 4 is first that occurs 2 times As at index = 4, 
# 4 has occurred atleast 2 times whereas at index = 6, 7 has occurred atleast 2 times.

# Input 2: N = 7, K = 1, A[] = {1, 7, 4, 3, 4, 8, 7}
# Output 2: 1


# steps
# dict = {
#     1:1,
#     7:1,
#     4:2,
#     3:1,
# }


def firstElementOccur(arr,k):
    arr = arr
    dictionary = {}
    for element in arr:
        if element in dictionary:
            dictionary[element] = dictionary[element]+1
        else:
            dictionary[element] = 1
        if dictionary[element] == k:
            return element
    return -1


print(firstElementOccur([1,7,4,3,4,8,7],2))