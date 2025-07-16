def threeSum(arr):
    arr.sort() #n(log(n))
    ans = []
    n = len(arr)
    unique = set()

    for i in range(n):
        left = i + 1
        right = n-1
        
        
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                triplet = (arr[i],arr[left],arr[right])
                if triplet not in unique:
                    unique.add(triplet)
                    ans.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
                
    return ans


# TC - O(n^2)
# Sc - O(n)

print(threeSum([-1,0,1,2,-1,-4]))