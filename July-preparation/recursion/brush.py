def print1N(n):
    if n <= 0:
        return n
    print1N(n-1)
    print(n)


# print1N(10)

def fact(n):
    if n<=1:
        return n
    
    return n * fact(n-1)

# print(fact(5))

def fibinoci(n):
    # 0,1,1,2,3 = 
    if n <= 1:
        return n
    
    return fibinoci(n-1) + fibinoci(n-2)


print(fibinoci(5))
    