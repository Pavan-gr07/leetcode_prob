# Here is a list of common pattern problems that you can solve, along with their respective diagrams and explanations:

# ### 1. **Right-angled Triangle Pattern**
#    - **Problem**: Print a right-angled triangle where the number of stars corresponds to the row number.
#    - **Diagram**:
#      ```    i    star
#      *      i=0   1
#      **     i=1   2
#      ***    i=2   3
#      ****   i=3   4
#      *****  i=4   5
#      ```
#    - **Explanation**: The first row has 1 star, the second row has 2 stars, and so on until the last row.
def patt1():
    for i in range(5):
        print("*"*(i+1))


# ### 2. **Inverted Right-angled Triangle**
#    - **Problem**: Print an inverted right-angled triangle pattern.
#    - **Diagram**:
#      ```     i   star
#      *****  i=0  5
#      ****   i=1  4
#      ***    i=2  3
#      **     i=3  2
#      *      i=4  1
#      ```         5-i
#    - **Explanation**: The first row starts with the maximum number of stars, and the number decreases by 1 in each subsequent row.
def patt2():
    for i in range(5):
        print("*"*(5-i))
# ### 3. **Pyramid Pattern**
#    - **Problem**: Print a pyramid pattern.
#    - **Diagram**:
#      ```        i    space    star
#          *      0     4        1
#         ***     1     3        3
#        *****    2     2        5
#       *******   3     1        7
#      *********  4     0        9
#      ```            n-i-1     2i+1
#    - **Explanation**: The number of stars starts from 1 and increases by 2 in each row, with spaces before the stars to create a centered pyramid shape.
def patt3():
    for i in range(5):
        print(" "*(5-i-1)+"*"*(2*i+1))
# ### 4. **Inverted Pyramid**
#    - **Problem**: Print an inverted pyramid pattern.
#    - **Diagram**:
#      ```          i   space   star
#      *********   i=0   0       9
#       *******    1     1       7       
#        *****     2     2       5
#         ***      3     3       3
#          *       4     4       1
#      ```               i       2*(n-i)-1
#    - **Explanation**: The first row starts with the maximum number of stars, and the number of stars decreases by 2 in each row, with leading spaces to center the pattern.

def patt4():
    for i in range(5):
        print(" "*(i)+"*"*(2*(5-i)-1))
# ### 5. **Hollow Square**
#    - **Problem**: Print a hollow square pattern.
#    - **Diagram**:
#      ```                               i    star
#      *****     i=0 and i=4 full star   i=0  5
#      *   *     j=0 and j=4 full star   i=1  2--0 and 4
#      *   *
#      *   *
#      *****
#      ```
#    - **Explanation**: The outer border is filled with stars, and the inside of the square is hollow (spaces in the middle).
def patt5():
    for i in range(5):
        for j in range(5):
            if i==0 or j==0 or i==4 or j==4:
                print("*",end="")
            else:
                print(" ",end="")
        print()
# ### 6. **Diamond Pattern**
#    - **Problem**: Print a diamond pattern.
#    - **Diagram**:
#      ```
#          *
#         ***
#        *****
#       *******
#      *********
#       *******
#        *****
#         ***
#          *
#      ```
#    - **Explanation**: The pattern consists of a pyramid at the top followed by an inverted pyramid to form a diamond shape.

def patt6():
    for i in range(5):
        print(" "*(5-i-1)+"*"*(2*i+1))
    for i in range(1,5):
        print(" "*(i)+"*"*(2*(5-i)-1))
    
# ### 7. **Pascal’s Triangle**
#    - **Problem**: Print Pascal’s Triangle.
#    - **Diagram**:
#      ```             space value  
#          1      i=0    4     i     1
#         1 1     i=1    3     i     2
#        1 2 1    i=2    2     i+j+i  3
#       1 3 3 1   i=3    1     i+j+j+i 4 
#      1 4 4 4 1  i=4    0     i+j+j+j+i 5
#      ```
#    - **Explanation**: Each number in Pascal's Triangle is the sum of the two numbers directly above it.
def patt7():
    for i in range(5):
        for j in range(5-i-1):
            print(" ",end=" ")
        for k in range(i+1):
            if  k==0 or k==i:
                print("1",end="  ")
            else:
                print(i,end="  ")
        print()

# ### 8. **Floyd’s Triangle**
#    - **Problem**: Print Floyd’s Triangle, a sequence of numbers in a triangle.
#    - **Diagram**:
#      ```
#      1              i=0 j=0 +1 = 1
#      2 3            i=1  j=0 +1 = 2 --- i=1 j=1 +1 = 3
#      4 5 6          i=2  j=0+1 = 
#      7 8 9 10
#      11 12 13 14 15
#      ```
#    - **Explanation**: Each row contains consecutive integers, starting from 1.
def patt8():
    count = 1
    for i in range(5):
        for j in range(i+1):
            print(f"{count}",end=" ")
            count +=1
        print()


# ### 9. **Butterfly Pattern**
#    - **Problem**: Print a butterfly pattern.
#    - **Diagram**:
#      ```          i    space   star
#      *       *    0     
#      **     **    1
#      ***   ***
#      **** ****
#      *********
#      **** ****
#      ***   ***
#      **     **
#      *       *
#      ```
#    - **Explanation**: The pattern is symmetric and consists of stars arranged in two halves, forming a butterfly shape.

def patt9a():
    for i in range(5 - 1):
        for j in range(4 * 5 - 1):
            # Print a star at position (i + 1) and (2n - (i + 1))
            if j <= i or j >= 2 * 5 - (i + 2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
           
#      *********   i=0 j=2n-1 
#      **** ****   i=1 j=8 -> n-i <-> 2n-i-1
#      ***   ***   i=3 j=
#      **     **
#      *       *
def patt9b():
    for i in range(5 - 2, -1, -1):
        for j in range(2 * 5 - 1):
            if j <= i or j >= 2 * 5 - i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def butterfly(n):
    # Upper part of the butterfly
    for i in range(1, n + 1):
        # Left wing
        # print(2 * (n - i))
        print("*" * i + f" " * (2 * (n - i)) + "*" * i)
        
    # # Lower part of the butterfly
    for i in range(n-1, 0, -1):
        # Right wing
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Example usage
# butterfly(5)


          
        # print(" "*(2*(5-i)-3)+"* "*(2*i+2))
        # print()
       
# ### 10. **Zigzag Pattern**
#    - **Problem**: Print a zigzag pattern.
#    - **Diagram**:
#      ```
#      *       *       *
#       *     * *     *
#        *   *   *   *
#         * *     * *
#          *       *
#      ```
#    - **Explanation**: The stars form a zigzag pattern where each row shifts the placement of stars in a certain direction.

def patt10():
    for i in range(5):
        row=""
        for j in range((2*5)*2):
            if j==i or j==2*5-(i+2) or j ==2*5+i or j==4*5-(i+2):
                row += "*"
            else:
                row +=" "
        print(row) 


                
# ### 11. **Number Pyramid**
#    - **Problem**: Print a pyramid pattern using numbers.
#    - **Diagram**:
#      ```
#          1
#         121
#        12321
#       1234321
#      123454321
#      ```
#    - **Explanation**: Each row consists of numbers that increase from 1 to a certain value and then decrease back to 1, forming a pyramid shape.

# def patt11():
#     for i in range(5):
#         count =2
#         for j in range(5-i-1):
#             print(" ",end=" ")
#         for k in range(2*i+1):
#             if  k==0 or k==2*i:
#                 print("1",end="  ")
#             else:
#                 print(count,end="  ")
#                 count += 1
#         print()

# ### 12. **Alphabet Pattern**
#    - **Problem**: Print an alphabet pattern.
#    - **Diagram**:
#      ```
#      A
#      AB
#      ABC
#      ABCD
#      ABCDE
#      ```
#    - **Explanation**: The first row prints 'A', the second row prints 'A' and 'B', and so on until the last row.

# ### 13. **Right-Angle Triangle with Numbers**
#    - **Problem**: Print a right-angled triangle using numbers.
#    - **Diagram**:
#      ```
#      1
#      12
#      123
#      1234
#      12345
#      ```
#    - **Explanation**: Each row contains consecutive numbers starting from 1 up to the row number.

def patt13():
    for i in range(1,5+1):
        for j in range(i):
            print(j+1,end="")
        print()

# ### 14. **Hollow Diamond Pattern**
#    - **Problem**: Print a hollow diamond pattern.
#    - **Diagram**:
#      ```
#          *
#         * *
#        *   *
#       *     *
#        *   *
#         * *
#          *
#      ```
#    - **Explanation**: The outer border of the diamond is made of stars, and the inside is hollow with spaces.
def patt14():
    for i in range(1,5+1):
        print(" "*(5-i)+"* "*(i))
    for i in range(5,0,-1):
        print(" "*(5-i)+"* "*(i))
# ---

# These 
# problems are great for practicing nested loops, conditionals, and understanding how to manage spaces and stars or numbers to create different patterns. By solving these, you will improve your understanding of loops, conditions, and how to format output.
patt14()