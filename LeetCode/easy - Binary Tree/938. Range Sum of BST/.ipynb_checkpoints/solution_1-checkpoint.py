# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # recursion
        self.res = 0
        
        def dfs(node, low, high):
            if node:
                if low <= node.val <= high:
                    self.res += node.val

                if low < node.val:
                    dfs(node.left, low, high)

                if node.val < high:
                    dfs(node.right, low, high)
                
        dfs(root, low, high)
        return self.res