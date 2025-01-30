
# 100. Find Greatest Common Divisor of Array
# Array
# Maths
# Google
# Amazon
# Bloomberg


# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Input 1: nums = [2,5,6,9,10]
# Output 1: 2
# Explanation 1: The smallest number in nums is 2. The largest number in nums is 10. The greatest common divisor of 2 and 10 is 2.

# Input 2: nums = [7,5,6,8,3]
# Output 2: 1
# Constraints:
# n == nums.length
# 2 <= n <= 103
# 1 <= nums[i] <= 103


        # Helper function to compute the greatest common divisor (GCD)
def gcd(x, y):
    while y:
        x, y = y, x % y
        return x
def gcdNum(arr):
    smallest = min(arr)
    greatest = max(arr)
    result = smallest
    while result:
        if smallest % result == 0 and greatest % result == 0 :
            break
        result -= 1
    return result

print(gcdNum([2,5,6,9,10]))