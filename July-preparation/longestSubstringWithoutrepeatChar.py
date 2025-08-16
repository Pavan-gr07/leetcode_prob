def longestChar(arr):
    left = 0
    right = 0
    unique = set(arr[left])
    ans = 0
    start =0
    while right < len(arr) and left < len(arr):
        if arr[right] not in unique:
            unique.add(arr[right])
            if right - left + 1 > ans:
                ans = right - left + 1
                start = left
            right += 1
        else:
            unique.remove(arr[left])
            left += 1

    longestSubString = arr[start : start + ans]
    return longestSubString, ans

print(longestChar("pwwkew"))



