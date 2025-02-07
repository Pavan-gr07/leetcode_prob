# printing N ugly numbers
def printNUglyNumbers(n):
    ans = []


    def checkUgly(num):
        if num<=0:
            return False
        for factors in [2,3,5]:
            while num % factors == 0:
                num //= factors
        return num == 1
    
    # O(Log(n))

    for i in range(1690):
        if len(ans) == n: break
        if checkUgly(i):
            ans.append(i)
 # O(n)
    return ans




# print(printNUglyNumbers(10))

# TC-O(n)

import heapq

def nth_ugly_number(n):
    ugly_numbers = []
    heap = [1]  # Min-heap to store ugly numbers
    seen = {1}  # Set to track numbers already added

    for _ in range(n):
        smallest = heapq.heappop(heap)  # Get the smallest ugly number
        ugly_numbers.append(smallest)

        # Generate new ugly numbers by multiplying by 2, 3, and 5
        for factor in [2, 3, 5]:
            new_ugly = smallest * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)

    return ugly_numbers  # Return list of first `n` ugly numbers

# Get the first 20 ugly numbers
# print(nth_ugly_number(20))


# using three pointers it can be reduce to O(n)
def generateUglyNumbers(n):
    ugly = [1] * n  # Array to store ugly numbers
    i2 = i3 = i5 = 0  # Pointers for multiples of 2, 3, and 5

    next2, next3, next5 = 2, 3, 5  # Next multiples of 2, 3, and 5

    for i in range(1, n):
        ugly[i] = min(next2, next3, next5)  # Pick the smallest next ugly number

        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2] * 2  # Move pointer for 2

        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3] * 3  # Move pointer for 3

        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5] * 5  # Move pointer for 5

    return ugly[n-1]  # Returns list of first n ugly numbers

# Test
n = 10
print(generateUglyNumbers(n))
