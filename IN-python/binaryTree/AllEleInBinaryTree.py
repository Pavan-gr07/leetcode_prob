# 1305. All Elements in Two Binary Search Trees
# Medium
# Topics
# Companies
# Hint
# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 

# Constraints:

# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def allElementsInBinarySearchTree(self,root1): 
        ans1 = []
        ans2 = []
        

        self.inOrder(root1,ans1)
        self.inOrder(root2,ans2)
        combined = sorted(ans1+ans2) 
        return combined

        # inOrder(root2,ans2)
    def inOrder(self,root,ans):
        if root:
            self.inOrder(root.left,ans)
            ans.append(root.val)
            self.inOrder(root.right,ans)





if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.right = TreeNode(8)


    root2 = TreeNode(8)
    root2.left = TreeNode(1)
    sol = Solution()
    print(sol.allElementsInBinarySearchTree(root1))