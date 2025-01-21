def factors(n):
    arr = []
    for i in range(1,n+1):
        if n%i==0:
            arr.append(i)
    return arr

# Tc- O(n)

def Factors(x):
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    return result

# TC - O(root(n))
print(Factors(21))
