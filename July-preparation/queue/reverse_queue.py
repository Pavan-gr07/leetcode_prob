# (Example: input `[1,2,3,4,5]` → output `[5,4,3,2,1]`)
from collections import deque
def reverse_queue(arr):
    temp = []

    
    while arr:
        temp.append(arr[0])
        arr.popleft()
    
    while temp:
        arr.append(temp.pop())

    return arr
    

if __name__ == "__main__":
    q = deque([5, 10, 15, 20, 25])
    
    print(reverse_queue(q))
    
    while q:
        print(q.popleft(), end=' ')