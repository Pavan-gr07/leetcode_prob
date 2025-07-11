def pattren():
    for i in range(4):
        for j in range(4):
            if i==0 or j==0:
                 print(f"*",end=" ")
            else:
                print(" ",end=" ")
        print()
pattren()