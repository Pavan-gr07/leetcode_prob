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
    def __init__(self,capacity):
        self.q = [None]* capacity
        self.front = -1
        self.rear = -1
        self.size = 0
        self.capacity = capacity
    
    def isEmpty(self):
        return self.size == 0
    

    def isFull(self):
        return self.size == self.capacity
    
    def append(self,x):
        if self.isFull():
            return "Queue is Full"
        
        if self.isEmpty():
             self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.q[self.rear] = x
        self.size += 1


    def appendLeft(self,x):
        if self.isFull():
            return "Queue is Full"
        
        if self.isEmpty():
             self.rear = self.front = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        
        self.q[self.front] = x
        self.size += 1

    def popleft(self):
        if self.isEmpty():
            return "is Empty"
        
        val = self.q[self.front]
        self.q[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
    
    def pop(self):
        if self.isEmpty():
            return "is Empty"
        
        val = self.q[self.rear]
        self.q[self.rear] = None

        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.rear = (self.rear - 1 +  self.capacity) % self.capacity
        self.size -= 1
        return val
    
dq = DoubleEndedNormalQueue(5)
dq.append(10)
dq.append(20)
dq.appendLeft(5)
dq.appendLeft(2)
print(dq.q)        # [5, 10, 20, None, 2]
print(dq.popleft())  # 2
print(dq.pop())      # 20
