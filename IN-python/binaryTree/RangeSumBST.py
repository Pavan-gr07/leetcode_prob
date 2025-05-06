# 938. Range Sum of BST
# Easy
# Topics
# Companies
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 1.4M
# Acceptance Rate
# 87.4%
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def rangeSumBST(self,root,low,high):
        ans=0
        def helper(root):
            nonlocal ans
            if not root:
                return None
            else:
                print(root.val,"root")
                # 
            if root.val >= low and root.val <= high:
                ans += root.val
            if root.val >= low:
                helper(root.left) 
                helper(root.right)
            return ans
           
        helper(root)
        return ans


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    sy = Solution()
    print(sy.rangeSumBST(root, 7,15))