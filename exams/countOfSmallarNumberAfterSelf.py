# 01. Count of Smaller Numbers After Self
# Array
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].



# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

# Input: nums = [-1]
# Output: [0]
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104




class CountSmaller:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        n = len(nums)
        counts = [0] * n
        indexes = list(range(n))

        def merge(start, mid,end):
            temp = []
            i,j = start, mid
            right_count = 0
            while i< mid and j < end:
                if nums[indexes[j]] < nums[indexes[i]]:
                    temp.append(indexes[j])
                    right_count += 1
                    j+=1
                else:
                    counts[indexes[i]] += right_count
                    temp.append(indexes[i])
                    i+=1

            while i < mid:
                counts[indexes[i]] += right_count
                temp.append(indexes[i])
                i+=1
            

            while j < end:
                temp.append(indexes[j])
                j+=1
            for i in range(len(temp)):
                indexes[start + i] = temp[i]
        
        def merge_sort(start, end):
            if end - start <= 1:
                return 
            mid = (start + end) // 2
            merge_sort(start ,mid)
            merge_sort(mid,end)
            merge(start,mid,end)


        merge_sort(0,n)
        return counts