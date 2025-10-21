# 3211. Generate Binary Strings Without Adjacent Zeros

# avatar
# Discuss Approach
# arrow-up
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer n.

# A binary string x is valid if all substrings of x of length 2 contain at least one "1".

# Return all valid strings with length n, in any order.

 

# Example 1:

# Input: n = 3

# Output: ["010","011","101","110","111"]

# Explanation:

# The valid strings of length 3 are: "010", "011", "101", "110", and "111".

# Example 2:

# Input: n = 1

# Output: ["0","1"]

# Explanation:

# The valid strings of length 1 are: "0" and "1".

 

# Constraints:

# 1 <= n <= 18

from collections import deque

def generate_binary_strings_without_adjacent_zeros(n):
    q = deque()
    q.append("")
    result = []
    while q:
        curr = q.popleft()
        if len(curr) == n:
            result.append(curr)
        else:
            q.append(curr + "1")
            if not curr or curr[-1] != "0":
                q.append(curr + "0")
            
    return result
    

print(generate_binary_strings_without_adjacent_zeros(3))