# 1497. Check If Array Pairs Are Divisible by k
# Medium
# Topics
# Companies
# Hint
# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.

 

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

# Constraints:

# arr.length == n
# 1 <= n <= 105
# n is even.
# -109 <= arr[i] <= 109
# # 1 <= k <= 105

# def arrDivisble(arr,k):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if ((arr[i]%k) + (arr[j]%k)) % k ==0:
#                 count +=1
#     print(count)
#     print(len(arr)//2)
#     if count == len(arr)//2:
#         return True
#     else:
#         return False

# print(arrDivisble([1,2,3,4,5,10,6,7,8,9],5))


def are_pairs_divisible_by_k(arr, k):
    # Edge case: If k is zero, division by zero is not allowed
    if k == 0:
        return False

    # Dictionary to count remainders
    remainder_count = [0] * k

    # Count remainders when divided by k
    for num in arr:
        remainder = num % k
        if remainder < 0:  # Ensure positive remainder
            remainder += k
        remainder_count[remainder] += 1
    print(remainder_count,"rem")

    # Check conditions for each remainder
    for i in range(k):
        if i == 0:  # Special case: remainder 0 must have an even count
            if remainder_count[i] % 2 != 0:
                return False
        elif k % 2 == 0 and i == k // 2:  # Special case: remainder k/2 must have an even count
            if remainder_count[i] % 2 != 0:
                return False
        else:  # Remainders i and k-i must have the same count
            if remainder_count[i] != remainder_count[k - i]:
                return False

    return True

# Example usage
array1 = [10, 25, 35, 55]
k1 = 5
print(are_pairs_divisible_by_k(array1, k1))  # Output: True

# array2 = [10, 25, 35, 55]
# k2 = 7
# print(are_pairs_divisible_by_k(array2, k2))  # Output: False
