from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()   # main queue
        self.q2 = deque()   # helper queue

    def push(self, x):
        # Step 1: Enqueue the new element into q2
        self.q2.append(x)

        # Step 2: Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return "Stack is Empty"
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            return "Stack is Empty"
        return self.q1[0]

    def isEmpty(self):
        return len(self.q1) == 0

    def display(self):
        return list(self.q1)

stack = StackUsingQueues()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.top()
stack.pop()
stack.top()
stack.top()