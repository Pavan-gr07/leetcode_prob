class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self,root):
        stack = []
        result = []
        current = root

        while current or stack:
            while current:  # Traverse to the leftmost node
                stack.append(current)
                current = current.left

            current = stack.pop()  # Process the leftmost node
            result.append(current.val)  # Visit the node

            current = current.right  # Move to the right subtree

        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sy = Solution()
    print(sy.inorderTraversal(root))