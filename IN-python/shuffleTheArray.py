def shuffleTheArray(nums):
    temp = [0]*len(nums)
    value = int(len(nums)/2)
    print(value)
    count = 0
    for num in nums:
        if count <=len(nums)-1:
           temp[count] = num
           count += 2

    count1 = 1
    for num in range(value,len(nums)):
        if count1 <= len(nums)-1:
           temp[count1] = nums[num]
           count1 += 2
    return temp



print(shuffleTheArray([2,5,1,3,4,7]))
