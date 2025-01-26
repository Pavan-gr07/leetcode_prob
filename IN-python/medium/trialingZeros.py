# 172. Factorial Trailing Zeroes
# Medium
# Topics
# Companies
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104
 

# Follow up: Could you write a solution that works in logarithmic time complexity?


# easy solution | beats 100%

# Surabhi Agarwal
# 365 Days Badge
# 20
# 21 hours ago
# Math
# C++
# Intuition
# The number of trailing zeroes in n! is determined by the number of factors of 10 in n!. A factor of 10 is created by multiplying 2 and 5. Since there are typically more factors of 2 than 5 in n!, the number of trailing zeroes is determined by the number of factors of 5.

# Approach
# Start by counting the factors of 5 in n, then in n/5, n/25, and so on.
# Each division adds the count of multiples of 5, 25, 125, etc., contributing to trailing zeroes.
# Use a loop that repeatedly divides n by 5 and sums up the results until n/5 
# k
#  <1.
# Complexity
# Time Complexity:
# O(log 
# 5
# ​
#  (n)), because the loop runs log 
# 5
# ​
#  (n) times.

# Space Complexity:
# O(1), as no extra space is used.

def factorialTrialingZeros(n):
    count = 0
    res=1
    for i in range(1,n+1):
        res = res * i
    arr = str(res)
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == "0":
            count+=1
        else:
            break
    return res

print(factorialTrialingZeros(7))

# The error occurs because Python's internal handling of integers for string conversion has limits when the number of digits is exceedingly large (as factorial grows very fast). Calculating the factorial directly is not an efficient approach for finding trailing zeroes since you only need the number of factors of 5 (and multiples of 5) in the factorial's prime factorization.

# Here’s why:
# - Trailing zeroes in `n!` are caused by factors of 10, which are produced by pairing factors of 2 and 5.
# - In factorials, there are always more factors of 2 than 5, so the number of trailing zeroes is determined by the number of factors of 5.

# A more efficient way to compute this avoids calculating the factorial directly. Instead, we count the number of multiples of 5, 25, 125, and so on, up to `n` (since higher powers of 5 contribute additional factors).

# If you're running into issues due to integer size limits, consider rewriting your logic as follows:

# ```python
# def trailingZeroes(self, n: int) -> int:
#     count = 0
#     while n > 0:
#         n //= 5
#         count += n
#     return count
# ```

# This approach avoids calculating the factorial itself and directly counts the number of trailing zeroes efficiently without hitting integer size limits.