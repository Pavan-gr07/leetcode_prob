# 108. Convert Sorted Array to Binary Search Tree
# Easy
# Topics
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.



class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def arrToBinaryTree(self,arr):

        def builtTree(start,end):
            if start> end:
                return None
            
            mid = (start+end)//2
            root = TreeNode(arr[mid])

            root.left = builtTree(start,mid-1)
            root.right = builtTree(mid+1,end)
            # for ele in arr
            return root
        return builtTree(0,len(arr)-1)
    def sortedArrToBinaryTree(self,arr):

        def builtTree(arr):
            if not arr:
                return None
            
            mid = len(arr)//2
            root = TreeNode(arr[mid])

            root.left = builtTree(arr[:mid])
            root.right = builtTree(arr[mid+1:])
            # for ele in arr
            return root
        return builtTree(arr)

    # Example usage:
def print_tree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.val))
        print_tree(node.left, level + 1, prefix="L--- ")
        print_tree(node.right, level + 1, prefix="R--- ")




if __name__ == "__main__":
    sol = Solution()
    tree = sol.sortedArrToBinaryTree([-10,-3,0,5,9])
    print_tree(tree)