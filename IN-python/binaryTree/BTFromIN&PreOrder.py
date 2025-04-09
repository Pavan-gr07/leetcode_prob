# 106. Construct Binary Tree from Inorder and preorder Traversal
# Medium
# Topics
# Companies
# Given two integer arrays inorder and preorder where inorder is the inorder traversal of a binary tree and preorder is the preorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# preorder.length == inorder.length
# -3000 <= inorder[i], preorder[i] <= 3000
# inorder and preorder consist of unique values.
# Each value of preorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# preorder is guaranteed to be the preorder traversal of the tree.

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

def buildTree(inorder, preorder):
    preorder.reverse()
    def solve(inorder,preorder):
        if not preorder or not inorder:
            return None
        root_val = preorder.pop()
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        root.left = solve(inorder[:inorder_idx],preorder)
        root.right = solve(inorder[inorder_idx+1:],preorder)
        return root
    
    return solve(inorder,preorder)
# Example usage:
inorder = [9, 3, 15, 20, 7]
preorder = [9, 15, 7, 20, 3]

root = buildTree(inorder, preorder)
print(root)

