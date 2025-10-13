class Queue():
    def __init__(self):
        self.arr = []
    
    def enqueue(self,x):
        self.arr.append(x)

    def dequeue(self):
        if not self.arr is None:
            return self.arr.pop(0)
        return "Queue is Empty"
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def front(self):
        if not self.isEmpty():
            return self.arr[0]
        return None
    
    def display(self):
        return self.arr
    

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, x):
        if self.isFull():
            return "Queue is Full"
        self.rear = (self.rear + 1) % self.capacity  # circular move
        self.arr[self.rear] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def getFront(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]

    def display(self):
        if self.isEmpty():
            return []
        result = []
        idx = self.front
        for _ in range(self.size):
            result.append(self.arr[idx])
            idx = (idx + 1) % self.capacity
        return result
