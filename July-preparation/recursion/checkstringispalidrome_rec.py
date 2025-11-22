


def validPalindrome(s):
    clean = ""
    for ch in s:
        if ch.isalnum():
            clean += ch
    left = 0
    right = len(clean) - 1
    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1
    return True
    

# using recursion

def validPalidrome(s):

    def check(s,l,r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return check(s,l+1,r-1)
    

print(validPalindrome("A man, a plan, a canal: Panama"))