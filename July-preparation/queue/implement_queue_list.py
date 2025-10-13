class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    

# Example usage:
q = Queue()     
q.enqueue(1)
q.enqueue(2)    
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.size())     # Output: 2


