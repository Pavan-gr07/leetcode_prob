# 249. Number of Steps to Reduce a Number to Zero
# Math
# Flipkart
# LinkedIn


# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.



# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Input: num = 8
# Output: 4

# Constraints:
# 0 <= num <= 106


def stepsToReduce(n):
    step = 0
    while n>0:
        if n %2 ==0:
            step +=1
            n /= 2
        else:
            n -= 1
            step +=1
    return step


print(stepsToReduce(8))