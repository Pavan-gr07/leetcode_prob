class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, var):
        self.stack = self.stack + [var]
        if not self.min_stack or var < self.min_stack[-1]:
            self.min_stack = self.min_stack + [var]

        

    def pop(self):
        if self.isEmpty():
            return None
        last_item = self.stack[-1]
        self.stack = self.stack[:-1]
        if self.min_stack and self.min_stack[-1] == last_item:
            self.min_stack = self.min_stack[ :-1]
        return last_item
        

    def top(self) :
        return self.stack if self.stack[-1] else None 

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def getMin(self) :
        return self.min_stack if self.min_stack[-1] else None 

        

# if __name__ == '__main__':
# Your MinStack object will be instantiated and called as such:
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.getMin()
stack.pop()
stack.top()
stack.getMin()