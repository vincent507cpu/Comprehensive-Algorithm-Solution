"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 使用全局变量
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_val = float('inf')
        self.min_root = None
        self.helper(root)
        return self.min_root

    def helper(self, node):
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)
        total = left + right + node.val

        if total < self.min_val:
            self.min_val = total
            self.min_root = node

        return total