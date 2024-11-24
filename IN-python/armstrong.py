def armstrong():
    nums_len = len(str(371))
    ans = 0
    for digit in str(371):
        ans += int(digit)**nums_len
    return ans == 371

print(armstrong())