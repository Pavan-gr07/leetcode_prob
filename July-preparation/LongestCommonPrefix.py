def commonPrefix(s):
    if len(s) <= 0:
        return ""

    for i in range(len(s[0])):
        for j in range(1, len(s)):
            if i >= len(s[j]) or s[0][i] != s[j][i]:
                return s[0][:i]
    return s[0]

print(commonPrefix(["dog", "racecar", "car"]))
