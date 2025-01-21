# 131. Immediate Smaller Element
# Math
# Google
# Amazon
# GoldmanSachs


# Given an integer array Arr of size N. For each element in the array, check whether the right adjacent element (on the next immediate position) of the array is smaller. If next element is smaller, update the current index to that element. If not, then -1.

# Input 1: Arr[] = {4, 2, 1, 5, 3}
# Output 1: 2 1 -1 3 -1
# Explanation 1: Array elements are 4, 2, 1, 5 3. Next to 4 is 2 which is smaller, so we print 2. Next of 2 is 1 which is smaller, so we print 1. Next of 1 is 5 which is greater, so we print -1. Next of 5 is 3 which is smaller, so we print 3. Note that for last element, output is always going to be -1 because there is no element on right.

# Input 2: Arr[] = {5, 6, 2, 3, 1, 7}
# Output 2: -1 2 -1 1 -1 -1
# Constraints:
# 1 <= N <= 105
# 1 <= Arr[i] <= 10


def immediate(arr):
    for i in range(len(arr)):
        if i!=len(arr)-1 and arr[i] > arr[i+1]:
                print(arr[i+1])
        else:
                print(-1)


immediate([5, 6, 2, 3, 1, 7])