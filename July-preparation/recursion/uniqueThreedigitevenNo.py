# 3483. Unique 3-Digit Even Numbers
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

# Example 1:

# Input: digits = [1,2,3,4]

# Output: 12

# Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

# Example 2:

# Input: digits = [0,2,2]

# Output: 2

# Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

# Example 3:

# Input: digits = [6,6,6]

# Output: 1

# Explanation: Only 666 can be formed.

# Example 4:

# Input: digits = [1,3,5]

# Output: 0

# Explanation: No even 3-digit numbers can be formed.

 

def findEvenNumbers(digits):
    from collections import Counter

    freq = Counter(digits)
    result = []

    # Generate all possible 3-digit even numbers
    for num in range(100, 1000):  
        if num % 2 != 0:  
            continue  # must be even

        # Extract digits
        h = num // 100
        t = (num // 10) % 10
        u = num % 10

        needed = Counter([h, t, u])

        # Check if digits are available
        is_valid = True
        for d in needed:
            if needed[d] > freq.get(d, 0):
                is_valid = False
                break

        if is_valid:
            result.append(num)

    return result


print(findEvenNumbers([2,1,3,0]))
