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
    def __init__(self, capacity):
        self.q = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.capacity - 1

    def append(self, x):
        if self.isFull():
            return "Queue is Full"
        
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        self.q[self.rear] = x

    def appendLeft(self, x):
        if self.isFull():
            return "Queue is Full"
        if self.front <= 0:
            return "Cannot insert at front (no space at left side)"
        self.front -= 1
        self.q[self.front] = x

    def popleft(self):
        if self.isEmpty():
            return "is Empty"
        val = self.q[self.front]
        self.q[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return val

    def pop(self):
        if self.isEmpty():
            return "is Empty"
        val = self.q[self.rear]
        self.q[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear -= 1
        return val

dq = DoubleEndedNormalQueue(5)
dq.append(10)
dq.append(20)
dq.appendLeft(5)
dq.appendLeft(2)
print(dq.q)        # [5, 10, 20, None, 2]
print(dq.popleft())  # 2
print(dq.pop())      # 20
