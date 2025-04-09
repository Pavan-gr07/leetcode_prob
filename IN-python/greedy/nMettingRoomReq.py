def minMettingRoom(a,b):
    a.sort()
    b.sort()
    p1=0
    p2=0
    mr=0
    res=0
    while p1<len(a):
        if a[p1] >= b[p2]:
            mr-=1
            p2+=1
        mr+=1
        p1+=1

    res = max(mr,res)
    return res



print(minMettingRoom([1,3,0,5,8,5],[2,4,6,7,9,9]))