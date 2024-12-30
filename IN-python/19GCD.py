def GCD(a,b):
    if b %a==0: return a
    return GCD(b%a,a)

print(GCD(24,25))
