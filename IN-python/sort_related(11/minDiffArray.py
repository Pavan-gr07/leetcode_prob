def mindiff(arr):
    ans=[]
    nums = sorted(arr)
    for i in range(len(nums)-1 ):  # Iterate up to the second-last element
       ans.append(nums[i + 1] - nums[i])  # Keep the sign
       

    return min(ans)


# Test the function
print(mindiff([25, 1, -1, 1, -1, 0, 1, 1, 1, 1, -1, -1, 0, -1, 1, 0, 15, -2, 2, -8, 1, 7, 10, 23, -23, 8]))
