def firstUnique(s):
    freq = {}

    for ele in s:
        # freq[ele] = freq.get(freq[ele], 0) + 1
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    print(freq)
    return -1

print(firstUnique("loveleetcode"))