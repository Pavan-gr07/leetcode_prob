# To find all factors of a given number, you can use the following Python code:


# ### Explanation:
# 1. **Loop through 1 to \( \sqrt{n} \):**
#    - For every \( i \), check if \( i \) divides \( n \) evenly (i.e., \( n \% i == 0 \)).
# 2. **Add both \( i \) and \( n // i \) to the list of factors:**
#    - \( i \) is the smaller factor.
#    - \( n // i \) is the corresponding larger factor.
# 3. **Avoid duplicates:**
#    - If \( i == n // i \), add it only once to avoid duplication.
# 4. **Sort the factors:**
#    - To present the factors in ascending order.

# ### Example:
# For \( n = 28 \):
# - Factors: \( 1, 2, 4, 7, 14, 28 \)

# **Steps:**
# 1. \( i = 1 \): \( 28 \% 1 = 0 \) → Add \( 1, 28 \)
# 2. \( i = 2 \): \( 28 \% 2 = 0 \) → Add \( 2, 14 \)
# 3. \( i = 3 \): \( 28 \% 3 \neq 0 \) → Skip
# 4. \( i = 4 \): \( 28 \% 4 = 0 \) → Add \( 4, 7 \)

# Output: `[1, 2, 4, 7, 14, 28]`


def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)  # Add the divisor
            if i != n // i:
                factors.append(n // i)  # Add the corresponding factor
    return sorted(factors)

print(find_factors(315))