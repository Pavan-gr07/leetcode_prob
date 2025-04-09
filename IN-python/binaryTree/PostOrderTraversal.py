# #94. Binary Tree PostOrder Traversal
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the PostOrder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?




class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def PostOrderTraversal(self,root):
        ans = []
        self.PostOrder(root,ans)
        return ans


    def PostOrder(self,root,ans):
        if root:
            self.PostOrder(root.left,ans)
            self.PostOrder(root.right,ans)
            ans.append(root.val)






if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)

    sy = Solution()
    print(sy.PostOrderTraversal(root))