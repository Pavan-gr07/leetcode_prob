


# arr = [[1,2,3],[4,5,6],[7,8,9]]
def spiralMatInput(arr):
    left ,right = 0,len(arr[0])-1
    top,bottom = 0,len(arr)-1
    ans =[]
    num=0

    while num<len(arr)*len(arr[0]):
        # l-r
        for i in range(left,right+1 ):
            ans.append(arr[top][i])
            num+=1
        top+=1


        # t r-b
        for i in range(top,bottom+1):
            ans.append(arr[i][right])
            num+=1  
        right-=1

        # b r-l 
        if top <= bottom:
            for i in range(right,left-1,-1):
                ans.append(arr[bottom][i])
                num+=1
            bottom-=1

        # b - top
        if left <= right:
            for i in range(bottom,top-1,-1):
                ans.append(arr[i][left])
                num+=1
            left+=1
    return ans
    

def spiralNumInput(n):
    arr = [[0]*n for _ in range(n)]
    num=1
    left ,right = 0,n-1
    top,bottom = 0,n-1


    while num<n*n:
        for i in range(left,right+1):
            arr[top][i] = num
            num+=1
        top+=1

        for i in range(top,bottom+1):
            arr[i][right] = num
            num+=1
        right-=1

        




    return arr

   
print(spiralNumInput(3))
# print(spiralMatInput(arr))