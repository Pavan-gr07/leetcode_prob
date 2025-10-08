class implementTwoStackQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def is_empty(self):
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def enqueue(self,item):
        self.input_stack.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        # is output stack is empty, pour all elements from input stack to output stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()
    
    def size(self):
        return len(self.input_stack) + len(self.output_stack)   
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]


# Example usage:
q = implementTwoStackQueue()
q.enqueue(1)
q.enqueue(2)        

q.enqueue(3)
print(q.dequeue())  # Output: 1 
print(q.size())     # Output: 2

print(q.peek())     # Output: 2
