# 60. Permutation Sequence
# Hard
# Topics
# Companies
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

 

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Example 3:

# Input: n = 3, k = 1
# Output: "123"
 

# Constraints:

# 1 <= n <= 9
# 1 <= k <= n!


# To solve the permutation sequence problem, we need to find the \( k \)-th permutation of numbers from \( 1 \) to \( n \).

# ### **Approach**
# 1. **Compute Factorials**: Since the total permutations of \( n \) numbers is \( n! \), we use factorials to determine which number should be placed at each position.
# 2. **Determine the Index**: The \( k \)-th permutation can be determined by dividing \( k \) by factorial values to pick the correct index at each step.
# 3. **Use a List of Numbers**: Maintain a list of available numbers, and pick elements based on the computed index.
# 4. **Adjust \( k \) to be Zero-Based**: Convert \( k \) to a zero-based index by decrementing it at the start.

# ### **Implementation**
# Here's a Python function to generate the \( k \)-th permutation sequence:

# ```python
# import math

def getPermutation(n: int, k: int) -> str:
    # Step 1: Generate factorials manually
    fact = [1] * n  # Store factorial values
    for i in range(1, n):
        fact[i] = fact[i - 1] * i  # Compute factorial iteratively
    
    # Step 2: Create a list of numbers
    numbers = [str(i) for i in range(1, n + 1)]
    
    # Step 3: Convert k to zero-based index
    k -= 1
    result = ""
    
    # Step 4: Construct permutation sequence
    for i in range(n, 0, -1):
        index = k // fact[i - 1]  # Find the correct index
        result += numbers[index]  # Append the chosen number
        
        # Remove element manually (shift left)
        for j in range(index, len(numbers) - 1):
            numbers[j] = numbers[j + 1]
        numbers.pop()  # Remove last element to shrink list
        
        k %= fact[i - 1]  # Update k for next iteration
    
    return result

# Example usage
print(getPermutation(3, 4))  # Output: "213"
print(getPermutation(4, 9))  # Output: "2314"


# ### **Explanation**
# For `n = 3, k = 3`:
# 1. Possible permutations: `["123", "132", "213", "231", "312", "321"]`
# 2. The 3rd permutation is `"213"`, which is correctly returned by the function.

# This approach runs in **O(n²)** due to list `pop()` operations but is efficient for small values of `n` (like 1 ≤ n ≤ 9).




# ************************************************* Approach *****************************************
### **How to Think Like This Step by Step**  

# When solving **the k-th permutation sequence**, we need to break the problem into logical steps. Let's walk through the thought process as a normal person would calculate this by hand.

# ---

# ## **Step 1: Understand the Total Number of Permutations**
# Each unique sequence of `n` numbers has **n!** (n factorial) permutations.  
# For example, when `n = 3`, we have:  
# \[
# 3! = 3 \times 2 \times 1 = 6
# \]
# Possible permutations:  
# `["123", "132", "213", "231", "312", "321"]`

# This tells us that the k-th permutation will be located **somewhere in this ordered list**.

# ---

# ## **Step 2: Identify How Many Groups Exist**
# Each **first digit** in the sequence occurs in blocks of **(n-1)!** permutations.  

# For example, when `n = 3`:
# - The first digit can be **1**, and the remaining two (`2,3`) can form **2! = 2** permutations: `"123", "132"`
# - The first digit can be **2**, and the remaining two (`1,3`) form **2! = 2** permutations: `"213", "231"`
# - The first digit can be **3**, and the remaining two (`1,2`) form **2! = 2** permutations: `"312", "321"`

# So, if `k = 3`, we know it must be in the second block (`213`, `231`).

# ---

# ## **Step 3: Compute the Index of the First Number**
# To determine the first digit:
# 1. **Convert `k` to zero-based** → **Subtract 1** from `k`
#    - If `k = 3`, it becomes `k = 2` (zero-based index).
# 2. **Find the group index** → Divide by `(n-1)!`
#    - `(2! = 2)`, so `index = 2 // 2 = 1`
#    - The **second number** in `[1,2,3]` is **"2"**.
# 3. **Remove "2"** from the list → Remaining numbers: `[1,3]`
# 4. **Update `k`** → `k = 2 % 2 = 0`

# ---

# ## **Step 4: Repeat for the Remaining Numbers**
# Now, we have a new list `[1,3]`, and we need the **0-th** permutation of these two numbers:
# 1. Since `n = 2`, there are `1! = 1` permutations per number.
# 2. **Find the next digit**: `index = k // 1 = 0`
#    - The first number in `[1,3]` is `"1"`, so we choose **"1"**.
# 3. **Remove "1"**, leaving `[3]`
# 4. **Update `k`** → `k = 0 % 1 = 0`

# Finally, only `"3"` is left. The answer is **"213"**.

# ---

# ## **General Formula**
# For `n` numbers:
# 1. Compute `(n-1)!`
# 2. Find `index = k // (n-1)!`
# 3. Choose that number and remove it from the list
# 4. Update `k = k % (n-1)!`
# 5. Repeat until all numbers are chosen

# ---

# ### **Thinking Like a Human**
# - **Breaking down** large problems into smaller ones makes them easier to solve.
# - **Pattern recognition**: Observing how digits change based on `k`.
# - **Divide and conquer**: Solve part of the problem at each step.

# This is how you can **think systematically** instead of guessing! 🚀