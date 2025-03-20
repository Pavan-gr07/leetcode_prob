from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        def dfs(node, path, paths):
            # Base case: If it's a leaf node, append the path to paths
            if not node.left and not node.right:
                paths.append("->".join(path))
                return
            
            # Recursive DFS for left and right children
            if node.left:
                dfs(node.left, path + [str(node.left.val)], paths)
            if node.right:
                dfs(node.right, path + [str(node.right.val)], paths)
        
        paths = []
        dfs(root, [str(root.val)], paths)
        return paths

# Example usage
if __name__ == "__main__":#this ensures script is run directly

    # Sample tree
    #       1
    #      / \
    #     2   3
    #      \ 
    #       5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    
    sol = Solution()
    print(sol.binaryTreePaths(root))  # Output: ["1->2->5", "1->3"]
