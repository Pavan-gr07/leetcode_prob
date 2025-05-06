# def searchInBinaryBoolean(self, root, val):
#     if not root:
#         print("Visited node: None")
#         return False

#     print(f"Visited node: {root.val}")  # Debug print to show current node

#     if root.val == val:
#         print(f"Found value: {val} at node: {root.val}")
#         return True

#     # Search in left and right subtrees
#     return self.searchInBinaryBoolean(root.left, val) or self.searchInBinaryBoolean(root.right, val)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def lowestCommonAncestor(self,root,p,q):
        print(f"Visiting Node: {root.val}")

        # If both p and q are greater than root, LCA lies in right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are less than root, LCA lies in left subtree
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # We are at the split point, this is the LCA
        else:
            print(f"LCA Found at Node: {root.val}")
            return root
    
if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.right = TreeNode(9)
    root.right.left = TreeNode(7)

    sy = Solution()
    print(sy.lowestCommonAncestor(root, root.right.left, root.right.right))