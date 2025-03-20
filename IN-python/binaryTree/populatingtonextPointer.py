from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # BFS using a queue
        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None
            for i in range(size):
                node = queue.popleft()
                # Link to the next node in the same level
                if prev:
                    prev.next = node
                prev = node
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

# Helper function to print tree levels
def print_tree_by_levels(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        result.append(level)
    return result

# Example usage
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

solution = Solution()
solution.connect(tree)

# Printing tree with next pointers (level by level)
print("Tree Levels with Next Pointers:")
print(print_tree_by_levels(tree))
