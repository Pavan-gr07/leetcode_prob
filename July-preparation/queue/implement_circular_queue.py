class MyCircularQueue():
    def __init__(self,k):
        self.k = k
        self.q = [None]*k
        self.rear = -1
        self.front = -1
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.k

    def enQueue(self,value):
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k

        self.q[self.rear] = value
        self.count += 1

        return True


    def deQueue(self):
        if self.isEmpty():
            return False
    
        if self.rear == self.front:
            self.rear = -1
            self.front = -1
        else:
            self.front = (self.front + 1) % self.k

        self.count -= 1
        return True
    
    def Front(self):
        if self.isEmpty():
            return -1

        return self.q[self.front]
    
    def Rear(self):
        if self.isEmpty():
            return -1
        
        return self.q[self.rear]
    
q = MyCircularQueue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.enqueue(40)
print(q.Front())  # 20
print(q.Rear())   # 40
