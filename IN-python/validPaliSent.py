def isPalindrome( s) :
        start = 0
        end = len(s) - 1

        while start < end:
            # Move the start pointer to the next valid character
            while start < end and not s[start].isalnum():
                start += 1
            print(start)
            # Move the end pointer to the previous valid character
            while start < end and not s[end].isalnum():
                end -= 1

            # Compare the characters at the start and end (case insensitive)
            if start < end and s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


print(isPalindrome("A man, a plan, a canal: Panama"))