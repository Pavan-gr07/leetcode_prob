# # 232. Implement Queue using Stacks
# Easy
# Topics
# Companies
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.



arr = [None]*10
rear = -1
def push(x):
    global rear
    if full():
        return None
    rear += 1
    arr[rear] = x
    

    
def pop():
    global rear
    if empty():
        return None
    front = arr[0]
    for i in range(rear):
        arr[i] = arr[i+1]
    arr[rear] = None
    rear -=1
    return front
   
def peek():
    global rear
    if empty():
        return None
    return arr[0]
   
def empty():
    global rear
    return rear == -1
        
def full():
    global rear
    return rear == 100




arr = [None]*10
rear = -1
def push(x):
    global rear
    if full():
        return None
    rear += 1
    arr[rear] = x

push(10)
push(20)
push(21)
push(22)
pop()
peek()
empty()

s1 =[]
s2 = []
def push1(x):
    while s1:
        s2.append(s1.pop())
    s1.append(x)
    while s2:
        s1.append(s2.pop())

def pop1():
    
    return s1.pop()
   
def peek1():
    return s1[-1]
   
def empty1():
    return not s1
 

push1(10)
push1(20)
push1(21)
push1(22)
pop1()
peek1()
empty1()


print(arr)