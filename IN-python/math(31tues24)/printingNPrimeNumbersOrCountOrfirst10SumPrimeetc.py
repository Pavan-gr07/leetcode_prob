def printingNPrimeNumbers(n):
    def isPrime(value):
        if value <= 1:
            return False
        for i in range(2, int(value**0.5) + 1):
            if value % i == 0:
                return False
        return True
    if n == 2:
        return 0
    ans = []
    num = 2
    while len(ans) < n:
        if isPrime(num):
            ans.append(num)
        num += 1

    return ans

# print(printingNPrimeNumbers(10))

# TC-O(N)



# Your current approach is inefficient because it checks the primality of each number up to `n` individually using a loop, making it **O(n√n)** in time complexity. Instead, we can use the **Sieve of Eratosthenes** algorithm, which runs in **O(n log log n)** time and is significantly faster.

# ### Optimized Solution: **Sieve of Eratosthenes**
# ```python
def countPrimes( n) :
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        print(int(n**0.5)+1)
        for i in range(2, int(n**0.5) + 1):# sq will like magical only that 
            if is_prime[i]:
                for j in range(i * i, n, i):  # Mark multiples of i as False
                    is_prime[j] = False
        print(is_prime)
        return sum(is_prime)

print(countPrimes(12))
# # Example usage:
# sol = Solution()
# print(sol.countPrimes(20))  # Output: 8 (Primes: 2, 3, 5, 7, 11, 13, 17, 19)
# ```

# ### Why is this faster?
# - **Instead of checking each number individually**, we mark the multiples of each prime starting from `2` as **non-prime**.
# - **Only iterate up to √n**, which drastically reduces operations.
# - **Uses an array (`is_prime`) to track prime numbers**, making marking operations efficient.

# #### **Time Complexity:**
# - **O(n log log n)** (much faster than your **O(n√n)** solution)

# This solution will run efficiently for large values of `n`, such as `10^6`. 🚀