def threeSumClosest(arr):
    target = 1
    arr.sort()
    n = len(arr)
    diffValue = float('inf')
    closest_sum = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            min_diff = abs(target - sum)
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return sum
            if min_diff < diffValue:
                diffValue = min_diff
                closest_sum = sum
            elif min_diff == diffValue and sum < target:
                diffValue = min_diff
                closest_sum = sum
    return closest_sum

print(threeSumClosest([-1,2,1,-4]))