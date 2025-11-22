def fact(n):
    if n ==0:
        return 1
    return n * fact(n - 1)

# print(fact(5))


def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n - 1)

# print(sumN(5))


def fibinocci(n):
    a = 0
    b = 1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n):
        s = a + b
        a = b
        b = s
        print(s,end=" ")
    


def fib(n):
    if n <= 1:
        return n
    
    a = fib(n-1)
    b = fib(n-2)
    return a + b



# Using DP

def fibdp(n, dp={}):
    if n <= 1:
        return n
    if n in dp:
        return dp[n]  
    a =   fibdp(n-1, dp)
    b =   fibdp(n-2, dp)      # reuse result
    dp[n] = a + b
    return dp[n]



# print(fibdp(4))


# reverse String
def reverseString(s):
    if s == "":
        return ""
    
    return reverseString(s[1:]) + s[0]


def reverseString(s):
    left, right = 0, len(s)-1

    while left < right:
        s[right],s[left] = s[left],s[right]
        left += 1
        right -= 1
    return s


def reverseAnArray(s):
    if len(s) == 0:
        return []
    rest = reverseAnArray(s[1:])
    rest.append(s[0])
    return rest

def reverse_array(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)

print(reverseAnArray(["h","e","l","l","o"]))
