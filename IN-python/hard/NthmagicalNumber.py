# # 
# 878. Nth Magical Number
# Hard
# Topics
# Companies
# A positive integer is magical if it is divisible by either a or b.

# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 1, a = 2, b = 3
# Output: 2
# Example 2:

# Input: n = 4, a = 2, b = 3
# Output: 6
 

def magicalNumber(a,b,n):
    i=1
    ans = 0
    num=2
    while i<=n:
        if num % a == 0  or num % b == 0:
            if i == n:
                ans = num
                break
            i+=1
        num += 1
    return ans

print(magicalNumber(40000,40000,1000000000))




# Here’s the Python code to solve the problem using **binary search** for efficiency:

# ```python
def nthMagicalNumber(n, a, b):
    MOD = 10**9 + 7

    # Helper function to compute the greatest common divisor (GCD)
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Compute the least common multiple (LCM) of a and b
    lcm = (a * b) // gcd(a, b)

    # Binary search for the nth magical number
    left, right = 1, n * min(a, b)
    while left < right:
        mid = (left + right) // 2
        # Count of magical numbers <= mid
        count = (mid // a) + (mid // b) - (mid // lcm)
        if count < n:
            left = mid + 1
        else:
            right = mid

    return left % MOD
# ```

# ### Example Usage:
# ```python
# # Test case 1
# n = 1
# a = 2
# b = 3
# print(nthMagicalNumber(n, a, b))  # Output: 2

# # Test case 2
# n = 4
# a = 2
# b = 3
# print(nthMagicalNumber(n, a, b))  # Output: 6
# ```

# ---

# ### Explanation of the Code:
# 1. **GCD and LCM**:
#    - Use the **GCD** (greatest common divisor) to calculate the **LCM** (least common multiple) of \( a \) and \( b \), which helps avoid counting duplicates.

# 2. **Binary Search**:
#    - Search within the range \([1, n \times \min(a, b)]\), since the nth magical number can't exceed this range.
#    - Use the midpoint \( \text{mid} \) to count how many magical numbers are less than or equal to \( \text{mid} \). The formula is:
#      \[
#      \text{count} = \left\lfloor \frac{\text{mid}}{a} \right\rfloor + \left\lfloor \frac{\text{mid}}{b} \right\rfloor - \left\lfloor \frac{\text{mid}}{\text{LCM}(a, b)} \right\rfloor
#      \]
#    - Adjust the binary search bounds based on whether the count is less than \( n \).

# 3. **Modulo**:
#    - Since the result may be very large, return the final answer modulo \( 10^9 + 7 \).

# This approach ensures efficiency with a time complexity of \( O(\log(n \times \min(a, b))) \).