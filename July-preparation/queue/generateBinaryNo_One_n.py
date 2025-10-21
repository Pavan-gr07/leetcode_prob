# Generate Binary Numbers
# Difficulty: EasyAccuracy: 67.48%Submissions: 64K+Points: 2
# Given a number n. The task is to generate all binary numbers with decimal values from 1 to n.

# Examples:

# Input: n = 4
# Output: ["1", "10", "11", "100"]
# Explanation: Binary numbers from 1 to 4 are 1, 10, 11 and 100.
# Input: n = 6
# Output: ["1", "10", "11", "100", "101", "110"]
# Explanation: Binary numbers from 1 to 6 are 1, 10, 11, 100, 101 and 110.
# Constraints:
# 1 ≤ n ≤ 106


from collections import deque
def generateBinaryNumbers(n):
    q = deque(['1'])
    result = []

    for i in range(1,n+1):
        front = q.popleft()
        result.append(front)
        q.append(front + "0")
        q.append(front + "1")

    return result


print(generateBinaryNumbers(16))


