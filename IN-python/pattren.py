
import math
# 00 01 02
# 10 11 12
# 20 21 22
def pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print(f"{i}{j}",end=" ")
        print()  
    return n

# * * * *
# * * * *
# * * * *
# * * * *
def pattern2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(f"*",end=" ")
        print()  
    return n


# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
def pattern3(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(f"*",end=" ")
        print()  
    return n    


# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
def pattern4(n):
    for i in range(0,n):
        for j in range(i+1):
            print(f"{j+1}",end=" ")
        print()  
    return n


#   * * * * * * * 
#     * * * * * *
#       * * * * *
#         * * * *
#           * * *
#             * *
#               *
def pattern5(n):    
    for i in range(0,n):
        for j in range(n):
            if j >i:
                 print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    return n


#   2 3 4 5 6 7 8 -i->0 j->
#     3 4 5 6 7 8
#       4 5 6 7 8
#         5 6 7 8
#           6 7 8
#             7 8
#               8

def pattern6(n):    
    for i in range(0,n):
        for j in range(n):
            if j >i:
                 print(f"{j+1}", end=" ")
            else:
                print(" ", end=" ")
        print()
    return n


#       *     i=0 -> j=1 
#     * * *   i=1 -> j=3
#   * * * * *  i=2 -> j=5
#  * * * * * * *  i=3 -> j=5
# * * * * * *  *  i=4 -> j=5
#     *
#    ***
#   *****
#  *******
# *********

# i   space  star
# 0    4      1
# 1    3      3
# 2    2      5
# 3    1      7
# 4    0      9
#     n-i-1   2i+1

# def pattern7(n):    
#     for i in range(0,n):
#         for j in range(n-i-1):
#                  print(f" ", end=" ")
#         for k in range(2*i+1):
#                  print(f"*", end=" ")
#         print()
#     return n
def pattern7(n):    
    for i in range(0,n):
        print(f" "*(n-i-1)+"*"*(2*i+1))
    # return n
# n=4
# *             i->0  j->1   star
# * *           i->1  j->2    
# * * *         i->2  j->3
# * * * *       i->3  j->4
# * * *         i->4  j->3
# * *           i->5  j->2
# *             i->6  j->1
            #    7/2 = 3.5 = 3 --> i+1
            #    7/2 = 3.5 = 3 --> n-i

def pattern8(n):    
    for i in range(2*n-1):
        stars = i+1
        if(i>=n):
             stars = 2*n-i-1
        for j in range(stars):
            print(f"*", end=" ")
        # if(i<=math.floor(n/2)):
        #      for j in range(i+1):
        #          print(f"*", end=" ")
        # else:
        #     for k in range(n-i):
        #          print(f"*", end=" ")
        print()
    return n     

#             i    space   star
#       *     0     2       1
#     * *     1     1       2
#   * * *     2     0       3
                #   n-i    i+1
def pattern10(n):
    for i in range(n):
        for j in range(n-i-1):
            print(f" ", end="")
        for k in range(i+1):
            print(f"*", end="")
        print()

#             i    space   star
# * * * *     0     0        4
#   * * *     1     1        3
#     * *     2     2        2
#       *     3     3        1
#                  
# def pattern11(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(f" ", end="")
#         for k in range(n-i):
#             print(f"*", end="")
#         print()
def pattern11(n):
    for i in range(n):
        print(f" "*(i+1)+"*"*(n-i))


#       *     0     3        1
#     * *     1     2        2
#   * * *     2     1        3
# * * * *     3     0        4
#   * * *     4     1        3
#     * *     5     2        2
#       *     6     3        1
#           if floor(n/2)==i -> n/2-i

def pattern9(n): 
    for i in range(n):
        for j in range(n-i-1):
            print(f" ", end="")
        for k in range(i+1):
            print(f"*", end="")   
        print()
    for i in range(n):
        for j in range(i+1):
            print(f" ", end="")
        for k in range(n-i):
            print(f"*", end="")
        print()
    return n 

def pattern9a(n): 
    # Upper part of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))
    
    # Lower part of the diamond
    for i in range(n - 1):  
        print(" " * (i + 1) + "*" * (n - i - 1))




n = int(input(("enter the number")))
pattern8(n)
