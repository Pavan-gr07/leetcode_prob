# 641. Design Circular Deque
# Medium
# Topics
# premium lock icon
# Companies
# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
 

# Example 1:

# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]

# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4
 

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.


class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
        self.k = k

        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.k) % self.k
        self.queue[self.front] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.rear = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1)  % self.k

        return True

        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.rear = (self.rear - 1 + self.k) % self.k
            
        return True


    def getFront(self) -> int:
        return -1 if self.isEmpty else self.q[self.front]
        

    def getRear(self) -> int:
        return -1 if self.isEmpty else self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.rear == -1 and self.front == -1 
        

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front
        


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(5)
param_1 = obj.insertFront(12)
param_2 = obj.insertLast(2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
print(param_5)
param_6 = obj.getRear()
print(obj.queue)
param_7 = obj.isEmpty()
param_8 = obj.isFull()