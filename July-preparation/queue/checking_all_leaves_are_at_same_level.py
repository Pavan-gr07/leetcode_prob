# Leaves at Same Level or Not
# Difficulty: EasyAccuracy: 39.47%Submissions: 131K+Points: 2
# Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. Return true if all leaf nodes are at the same level, and false otherwise.

# Examples :

# Input: root = [1, 2, 3]
#     1
#    / \
#   2   3
# Output: true
# Explanation: The binary tree has a height of 2 and the leaves are at the same level.
# Input: root = [10, 20, 30, 10, 15, N, N]
#     10
#    /  \
#  20   30
#  /  \
#  10   15
# Output: false
# Explanation: The binary tree has a height of 3 and the leaves are not at the same level.
# Input: root = [3, 2, 1]
#     3
#    / \
#   2   1
# Output: true
# Explanation: The binary tree has a height of 2 and the leaves are at the same level.
# Constraints:
# 1 ≤ n ≤ 105


def checkLeavesAtSameLevel(root):
    if not root:
        return True

    from collections import deque
    queue = deque()
    queue.append((root, 0))
    leaf_level = None

    while queue:
        node, level = queue.popleft()

        if not node.left and not node.right:  # Leaf node
            if leaf_level is None:
                leaf_level = level
            elif leaf_level != level:
                return False

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return True 