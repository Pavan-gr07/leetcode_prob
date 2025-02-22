# 155. Min Stack
# Medium
# Topics
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class Stack:
    def __init__(self):
        self.s = []  # Main stack
        self.min_stack = []  # Stack to track min values

    def push(self, x):
        self.s.append(x)
        # If min_stack is empty OR x is smaller/equal to the current min, push to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.s:
            print("Stack Underflow")
            return None
        val = self.s.pop()
        # If popped value was the min, remove from min_stack as well
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def getMin(self):
        if not self.min_stack:
            print("Stack is empty")
            return None
        return self.min_stack[-1]  # Top of min_stack has the current min
