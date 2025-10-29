# Perfect 🔥 — let’s do **both Min and Max Priority Queues** using `heapq` (Python’s built-in heap module).

# By default, `heapq` in Python is a **Min Heap**, meaning the smallest value has the *highest priority*.
# For a **Max Heap**, we just store *negative priorities* to reverse the order.

# ---

# ### ✅ **Min Priority Queue**

# ```python
# import heapq

# class MinPriorityQueue:
#     def __init__(self):
#         self.heap = []

#     def push(self, value, priority):
#         # Heap stores tuples (priority, value)
#         heapq.heappush(self.heap, (priority, value))

#     def pop(self):
#         if not self.heap:
#             return "Queue is empty"
#         return heapq.heappop(self.heap)  # Removes smallest priority

#     def peek(self):
#         if not self.heap:
#             return "Queue is empty"
#         return self.heap[0]  # Smallest element (min priority)

#     def isEmpty(self):
#         return len(self.heap) == 0
# ```

# 🧩 **Example:**

# ```python
# pq = MinPriorityQueue()
# pq.push("Task A", 3)
# pq.push("Task B", 1)
# pq.push("Task C", 2)

# print(pq.pop())  # (1, 'Task B')
# print(pq.pop())  # (2, 'Task C')
# print(pq.pop())  # (3, 'Task A')
# ```

# ---

# ### ✅ **Max Priority Queue**

# We can make a **Max Heap** easily by pushing **negative priorities**.

# ```python
# import heapq

# class MaxPriorityQueue:
#     def __init__(self):
#         self.heap = []

#     def push(self, value, priority):
#         # Push negative priority to invert min-heap to max-heap
#         heapq.heappush(self.heap, (-priority, value))

#     def pop(self):
#         if not self.heap:
#             return "Queue is empty"
#         priority, value = heapq.heappop(self.heap)
#         return (-priority, value)  # Convert back to positive priority

#     def peek(self):
#         if not self.heap:
#             return "Queue is empty"
#         priority, value = self.heap[0]
#         return (-priority, value)

#     def isEmpty(self):
#         return len(self.heap) == 0
# ```

# 🧩 **Example:**

# ```python
# pq = MaxPriorityQueue()
# pq.push("Task A", 3)
# pq.push("Task B", 1)
# pq.push("Task C", 2)

# print(pq.pop())  # (3, 'Task A')
# print(pq.pop())  # (2, 'Task C')
# print(pq.pop())  # (1, 'Task B')
# ```

# ---

# ✅ **Summary of Difference:**

# | Type      | Priority Stored      | Removes           |
# | --------- | -------------------- | ----------------- |
# | Min Queue | `(priority, value)`  | Smallest priority |
# | Max Queue | `(-priority, value)` | Largest priority  |

# ---

# Would you like me to show a **single class** that can switch between *min* and *max* mode based on a flag (like `mode='min'` or `mode='max'`)?
