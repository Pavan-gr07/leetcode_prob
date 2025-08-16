def monotonic_decreasing_stack(arr):
    stack = []
    result = [] # Or process elements as they are popped
    for element in arr:
        while stack and stack[-1] > element: # For decreasing, pop if top is smaller
            stack.pop() # Process popped elements if needed
        stack.append(element)
        # You might add elements to 'result' here based on problem needs
    return stack # Or return 'result' depending on the problem


print(monotonic_decreasing_stack([2, 1, 2, 4, 3]))