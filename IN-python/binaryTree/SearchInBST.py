# 700. Search in a Binary Search Tree
# Easy
# Topics
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():   
    def searchInBinary(self,root,val):
        # Base case: if root is None or we found the value
        if not root or root.val == val:
            return root
        
        # Search in the left subtree
        left_result = self.searchInBinary(root.left, val)
        if left_result:
            return left_result
        
        # Search in the right subtree
        right_result = self.searchInBinary(root.right, val)
        if right_result:
            return right_result
        
        # If not found in either subtree, return None
        return None
    def searchInBinaryBoolean(self,root,val):
        # Base case: if root is None or we found the value
        if not root :
            return None
        
        if root.val == val:
            return True
        # Search in the left subtree
        left_found = self.searchInBinaryBoolean(root.left, val)
        if left_found:
            return True
        
        
        # Search in the right subtree
        right_found=self.searchInBinaryBoolean(root.right, val)
        if right_found:
            return True
        
        # If not found in either subtree, return None
        return False
    def searchInBinaryBoolean1(self, root, val):
        if not root:
            print("Visited node: None")
            return False

        print(f"Visited node: {root.val}")  # Debug print to show current node

        if root.val == val:
            print(f"Found value: {val} at node: {root.val}")
            return True

        # Search in left and right subtrees
        return self.searchInBinaryBoolean1(root.left, val) or self.searchInBinaryBoolean1(root.right, val)



if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left= TreeNode(1)
    root.left.right= TreeNode(3)
    
    sol = Solution()
    print(sol.searchInBinaryBoolean1(root,7))

