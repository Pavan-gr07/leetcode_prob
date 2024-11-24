def firstNSum(n):
    sum = 0
    
    sum =n*(n+1)/2
    return sum


print("Enter Your Number ")
x=int(input())
result = firstNSum(x)
print(result)