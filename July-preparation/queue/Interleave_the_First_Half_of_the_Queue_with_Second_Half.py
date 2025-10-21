# Interleave the First Half of the Queue with Second Half
# Difficulty: MediumAccuracy: 62.41%Submissions: 17K+Points: 4Average Time: 20m
# Given a queue q[] of even size. Your task is to rearrange the queue by interleaving its first half with the second half.

# Interleaving is the process of mixing two sequences by alternating their elements while preserving their relative order.
# In other words, Interleaving means place the first element from the first half and then first element from the 2nd half and again second element from the first half and then second element from the 2nd half and so on....

# Examples:

# Input: q[] = [2, 4, 3, 1]
# Output: [2, 3, 4, 1]
# Explanation: We place the first element of the first half 2 and after that 
# place the first element of second half 3 and after that repeat
# the same process one more time so the resulting queue will be [2, 3, 4, 1]
# Input: q[] = [3, 5]
# Output: [3, 5]
# Explanation: We place the first element of the first half 3 and first element
# of the second half 5 so the resulting queue is [3, 5]
# Constraints:
# 1 ≤ queue.size() ≤ 103
# 1 ≤ queue[i] ≤ 105

from collections import deque

def rearrangeQueue(arr):
    l = len(arr)
    aux = deque(arr[:l//2])
    main = deque(arr[l//2:])
    
    while aux:
        main.append(aux.popleft())
        main.append(main.popleft())
    
    return main


# in hacker rank it a deque in the parameter not a list
def rearrangeQueue(arr):
    l = len(arr)
    aux = deque()

    for _ in range(l//2):
        aux.append(arr.popleft())
    
    while aux:
        arr.append(aux.popleft())
        arr.append(arr.popleft())
    
    return arr


print(rearrangeQueue(deque([2, 4, 3, 1])))


# ############################  Taking Reference from Chat GPT ##########################################



# Excellent question 👏

# Let’s break it down simply 👇

# An **auxiliary queue** just means —
# ➡️ an **extra / helper queue** used temporarily to hold some elements while you manipulate the main queue.

# It doesn’t change how queues work — it’s just a second one you create to make your logic easier.

# ### Example (Interleave halves)

# Say you have this main queue:

# ```
# [1, 2, 3, 4, 5, 6]
# ```

# ✅ Step 1 — Take the **first half** (`[1, 2, 3]`) and put it into an **auxiliary queue**.

# ```
# aux = [1, 2, 3]
# main = [4, 5, 6]
# ```

# ✅ Step 2 — Now interleave:

# * Pop from `aux` → 1 → enqueue to `main`
# * Pop from `main` → 4 → enqueue to `main`
# * Pop from `aux` → 2 → enqueue to `main`
# * Pop from `main` → 5 → enqueue to `main`
# * Pop from `aux` → 3 → enqueue to `main`
# * Pop from `main` → 6 → enqueue to `main`

# Result:

# ```
# main = [1, 4, 2, 5, 3, 6]
# ```

# So, the **auxiliary queue** is just a *temporary* helper queue you use to store part of the data while processing.

# Would you like me to show you the exact Python implementation using `collections.deque` for this?
