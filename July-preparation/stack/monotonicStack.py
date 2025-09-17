def monotonic_decreasing_stack(arr):
    stack = []
    result = [] # Or process elements as they are popped
    for element in arr:
        while stack and stack[-1] < element: # For decreasing, pop if top is smaller
            stack.pop() # Process popped elements if needed
        stack.append(element)
        # You might add elements to 'result' here based on problem needs
    return stack # Or return 'result' depending on the problem


print(monotonic_decreasing_stack([1,2,1]))


# Decreasing Monotonic Stack

# Top of stack is always smaller than the one below.

# Use this for Next Greater Element.

# Why? Because when we see a bigger number, we pop all smaller ones since they can’t be “next greater” for anyone anymore.

# Increasing Monotonic Stack

# Top of stack is always bigger than the one below.

# Use this for Next Smaller Element.

# Why? Because when we see a smaller number, we pop all bigger ones since they can’t be “next smaller” anymore.