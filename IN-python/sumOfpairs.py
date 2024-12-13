arr = [3,2,1,7]
k=9

mx = max(arr)
attend =[False]*(mx+1)
for num in arr:
    if num <= mx:
        attend[num] = True
found = False
for num in arr:
    if k>num and k-num<=mx and attend[k-num]:
        print("True")
        found = True
        break
if not found:
    print("False")
        

        