# 230. Kth Smallest Element in a BST
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.8M
# Submissions
# 2.4M
# Acceptance Rate
# 74.9%
# Topics
# Companies
# Hint 1
# Hint 2
# Hint 3
# Hint 4

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallestElement(root,k):
    ans = []
    def inOrder(root,ans):
        if not root:
             return None
        root.left = inOrder(root.left,ans)
        ans.append(root.val)
        root.right = inOrder(root.right,ans)
    inOrder(root,ans)
    return ans[k-1]


def print_tree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.val))
        print_tree(node.left, level + 1, prefix="L--- ")
        print_tree(node.right, level + 1, prefix="R--- ")


# Driver Code
if __name__ == '__main__':
	
	# binary tree formation 
	root = TreeNode(5) 
	root.left = TreeNode(3) 
	root.right = TreeNode(6) 
	root.left.left = TreeNode(2) 
	root.left.right = TreeNode(4) 
	root.left.left.left= TreeNode(1) 
		
	x = 3
	print(kthSmallestElement(root, x))

