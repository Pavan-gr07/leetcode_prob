def max_len_zero_sum_subarray(arr):
    # Initialize variables
    hash_map = {}
    max_len = 0
    curr_sum = 0
    for i in range(len(arr)):
        # Update cumulative sum
        curr_sum += arr[i]

        print(hash_map)
        # Check if cumulative sum is 0
        if curr_sum == 0:
            max_len = i + 1
        dict = {15:1,16:2}
        
        # # If sum is already in the hash map, update max_len
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            # Store the current sum with the index
            hash_map[curr_sum] = i

    return max_len

# Example Usage
arr = [15, -2, 2, -8, 1, 7, 10, 23]
print("Length of longest subarray with 0 sum:", max_len_zero_sum_subarray(arr))  # Output: 5
