# Given an array of n distinct and positive elements, the task is to find pair whose sum already exists in the given array. 

# Examples : 

# Input : arr[] = {2, 8, 7, 1, 5};
# Output : 2 5
#          7 1    
     
# Input : arr[] = {7, 8, 5, 9, 11};
# Output : Not Exist

def sumAlreadyExist(arr):
    ans =[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum_val = arr[i]+arr[j]
            for ele in arr:
                if ele == sum_val:
                    ans.append([arr[i],arr[j]])

    return ans                
# TC - O(n^3)
# SC - O(n)

def sumAlreadyExist1(arr):
    hash = set(arr)
    ans =[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum_val = arr[i]+arr[j]
            if sum_val in hash:
                ans.append([arr[i],arr[j]])

    return ans 

# TC - O(n^2)
# Sc - O(n)
print(sumAlreadyExist1([2,8,7,1,5]))