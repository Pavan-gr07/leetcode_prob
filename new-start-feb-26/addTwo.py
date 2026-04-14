def twoSum( nums, target):
    ans = []
    for i in range(len(nums)):
        for  j in range(1,len(nums)):
            if i!= j and nums[i] +  nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans

# print(twoSum([2,7,11,15],9))


# TC - O(n^2)
# SC - O(n)


def newTwoSum(nums,target):
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i


    for i in range(len(nums)):
        index = target - nums[i]
        if(index in dic and dic[index] != i ):
            return [dic[index],i]

print(newTwoSum([3,2,4],6))



# TC - O(n)
# SC - O(n)