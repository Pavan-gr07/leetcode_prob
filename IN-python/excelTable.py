def convertToTitle(columnNumber):
    title = ""
    while columnNumber > 0:
        # print(columnNumber,"column")
        # Adjust for 1-based indexing
        columnNumber -= 1
        # Find the remainder and convert to a character
        remainder = columnNumber % 26
        print(chr(9+65))
        title = chr(remainder + ord('A')) + title
        # Update columnNumber for the next iteration
        columnNumber //= 26

    
    return title

# # Example usage
result = convertToTitle(10)
print(result)  # Output: AB
# def titleToNumber(columnTitle):
#     number = 0
#     length = len(columnTitle)
#     for i in range(length):
#         # Convert each character to its corresponding number
#         value = ord(columnTitle[i]) - ord('A') + 1
#         # Update the number based on its position
#         number = number * 26 + value
        
#     return number

# # Example usage
# result = titleToNumber("AB")
# print(result)  # Output: 28
