def reverse(n):
    ans=0
    rev = 0
    n = abs(n)
    is_negative = n < 0
    while n:
        rev = n % 10
        ans = ans * 10 + rev
        n = n // 10
    if is_negative:
        ans = -ans 
    return ans

print(reverse(-123))

