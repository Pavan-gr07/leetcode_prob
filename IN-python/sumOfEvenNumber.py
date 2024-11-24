def sumOfEvenNumber(n):
    sum = 0

    for i in range(2,n+1,2):
        sum += i
        print(i)
    return sum
    
result = sumOfEvenNumber(6)
print(result)