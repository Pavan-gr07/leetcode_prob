# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium
# Topics
# Companies
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 777K
# Submissions
# 1.2M
# Acceptance Rate
# 65.8%

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()  # Get the last element as the root
    root = TreeNode(root_val)

    inorder_index = inorder.index(root_val)  # Find root in inorder

    # Build right subtree first (because postorder is Left-Right-Root)
    root.right = buildTree(inorder[inorder_index + 1:], postorder)
    root.left = buildTree(inorder[:inorder_index], postorder)
    
    return root

# Example usage:
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = buildTree(inorder, postorder)
print(root)

