# Implement a Deque (Double-ended Queue)

# Using List
class DoubleEndedQueue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0
        
    def append(self,x):
        self.q.append(x)



    def appendleft(self,x):
        self.q.insert(0,x)

    
    def pop(self):
        if self.isEmpty():
            return "Queue is empty"
        
        return self.q.pop()
    
    def popleft(self):
        if self.isEmpty():
            return "Queue is empty"
        
        return self.q.pop(0)



# using Normal Queue
class DoubleEndedNormalQueue:
    def __init__(self,size):
        self.q = [None]*size
        self.front = -1
        self.rear = -1
    
    def isEmpty(self):
        len
