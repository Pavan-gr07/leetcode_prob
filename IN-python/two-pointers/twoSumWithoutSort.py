def twoSum( nums, target):
        num_map = {}  # Dictionary to store value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                print(num_map,"nummap")
                return [num_map[complement], i]  # Return indices
            num_map[num] = i  # Store index of current number
        
        return []  # No solution found

print(twoSum([2,7,11,15],9))