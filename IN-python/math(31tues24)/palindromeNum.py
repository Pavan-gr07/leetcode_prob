def palindrome(n):
    # val=0,res=0
    rev = 0
    temp = 0
    while n > 0 :
        dig = n % 10
        rev = rev*10 + dig
        n //= 10
    return rev == temp

print(palindrome(121))