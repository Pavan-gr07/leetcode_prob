def fequency(arr):
    frequency={}

    for num in arr:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num] = 1


    return frequency


arr = [1,2,3,4,45,32,1,2,12,1,2]
result = fequency(arr)

print(result)

