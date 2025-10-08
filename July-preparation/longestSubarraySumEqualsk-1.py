def longestSubarraySumEqualsk(arr,k):
    cur_sum =0
    max_len = 0
    dict ={0:1}
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum - k in dict:
            diff = i - dict[cur_sum - k]
            if diff > max_len:
                max_len = diff
        if cur_sum not in dict:
            dict[cur_sum ] = i

    return max_len

print(longestSubarraySumEqualsk([94,-33,-13,40,-82,94,-33,-13,40,-82],52))