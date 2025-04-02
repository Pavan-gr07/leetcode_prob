# 110. Balanced Binary Tree
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0  # Height of empty subtree is 0
            leftHeight = checkHeight(node.left)
            rightHeight = checkHeight(node.right)
            
            # Check if the subtree rooted at 'node' is balanced
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1  # Subtree is unbalanced, propagate -1
            
            return max(leftHeight, rightHeight) + 1  # Height of current node
        
        return checkHeight(root) != -1
    
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.isBalanced(root)) 