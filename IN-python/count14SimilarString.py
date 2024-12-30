# 63. Count Pairs Of Similar Strings
# String
# Amazon
# Paytm


# You are given a 0-indexed string array words.

# Two strings are similar if they consist of the same characters.

# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.

# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.



# Input: words = ["aba","aabb","abcd","bac","aabc"]
# Output: 2

# Input: words = ["aabb","ab","ba"]
# Output: 3

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consist of only lowercase English letters.



def countPairsSimilarString(arr):
    from collections import Counter
    signatures = ["".join(sorted(set(word))) for word in arr]

    signature_count = Counter(signatures)
    print(signature_count)
    total_pairs = 0
    for i in signature_count.values():
        if i > 0:
            total_pairs += (i*(i-1)//2)
    return total_pairs




print(countPairsSimilarString(["aba","aabb","abcd","bac","aabc"]))