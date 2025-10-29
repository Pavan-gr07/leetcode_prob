# Perfect, Pavan 😎 — great next move!
# Implementing a **Priority Queue** is an excellent step after learning normal and circular queues — because it’s conceptually similar but introduces *ordering by priority*.

# Let’s walk through this clearly so you can implement it confidently 👇

# ---

# ## 🔹 What is a Priority Queue?

# A **Priority Queue** is a special kind of queue where **each element has a priority**, and:

# * In a **min-priority queue**, the *smallest* priority value is dequeued first.
# * In a **max-priority queue**, the *largest* priority value is dequeued first.

# So, unlike normal queues (FIFO), **order depends on priority, not insertion time**.

# ---

# ## 🧠 Ways to Implement

# You can implement a priority queue in three main ways:

# | Approach                   | Insertion | Deletion (Extract-Min/Max) | Structure                    |
# | -------------------------- | --------- | -------------------------- | ---------------------------- |
# | **1. Unsorted array/list** | O(1)      | O(n)                       | Simple, but slow removal     |
# | **2. Sorted array/list**   | O(n)      | O(1)                       | Fast removal, slow insertion |
# | **3. Binary Heap (best)**  | O(log n)  | O(log n)                   | Efficient for both           |

# ---

# ## 🔹 Start Simple — Using a List

# Here’s a **basic implementation** (min-priority queue) using a list, without using `heapq`:

# ```python
# class PriorityQueue:
#     def __init__(self):
#         self.q = []

#     def isEmpty(self):
#         return len(self.q) == 0

#     def push(self, value, priority):
#         # Add as tuple (priority, value)
#         self.q.append((priority, value))

#     def pop(self):
#         if self.isEmpty():
#             return "Queue is empty"

#         # Find minimum priority element
#         min_index = 0
#         for i in range(1, len(self.q)):
#             if self.q[i][0] < self.q[min_index][0]:
#                 min_index = i
        
#         # Remove and return it
#         return self.q.pop(min_index)

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         min_priority = min(self.q, key=lambda x: x[0])
#         return min_priority
# ```

# ---

# ### Example Run:

# ```python
# pq = PriorityQueue()
# pq.push("Task A", 3)
# pq.push("Task B", 1)
# pq.push("Task C", 2)

# print(pq.pop())  # → ('Task B', 1)
# print(pq.pop())  # → ('Task C', 2)
# print(pq.pop())  # → ('Task A', 3)
# ```

# ✅ Works as a **Min Priority Queue**

# ---

# ## 🔸 Want to make it a **Max Priority Queue**?

# Just change this comparison:

# ```python
# if self.q[i][0] > self.q[max_index][0]:
# ```

# and name it `MaxPriorityQueue`.

# ---

# ## 🔹 Next Level (Using `heapq`)

# Once you’re comfortable with the logic above, you can move to the efficient **heap** implementation:

# ```python
# import heapq

# class MinPriorityQueue:
#     def __init__(self):
#         self.heap = []

#     def push(self, value, priority):
#         heapq.heappush(self.heap, (priority, value))

#     def pop(self):
#         return heapq.heappop(self.heap)

#     def peek(self):
#         return self.heap[0] if self.heap else None
# ```

# This is how Python’s built-in `heapq` makes a real **priority queue** (backed by a binary heap).

# ---

# Would you like to start by implementing the **basic list-based one** manually (so you understand logic clearly) or jump directly into the **heap version** (which is efficient but less transparent)?

############################# Priority MIN Queue #########################################

class PriorityQueue:

    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0
    
    def push(self,value,priority):
        self.q.append((priority, value))

    def pop(self):

        if self.isEmpty():
            return "Queue is Empty"
        
        min_index = 0
        for i in range(1, len(self.q)):
            if self.q[i][0] < self.q[min_index][0]:
                min_index = i

        
        return self.q[min_index]
    
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"

        min_priority = min(self.q, key=lambda x : x[0])

        return min_priority


        
pq = PriorityQueue()
pq.push("Task A", 3)
pq.push("Task B", 1)
pq.push("Task C", 2)

print(pq.pop())  # → ('Task B', 1)
print(pq.pop())  # → ('Task C', 2)
print(pq.pop())  # → ('Task A', 3)


################################### Using heapq #########################################
import heapq
class PriorityQueUsingHeapq:
    def __init__(self):
        self.q = []

    def push(self,priority,value):
        heapq.heappush(self.q,(priority,value))

    def pop(self):
        heapq.heappop(self.q)

    
    def peek(self):
        return self.heap[0] if self.q else None
    