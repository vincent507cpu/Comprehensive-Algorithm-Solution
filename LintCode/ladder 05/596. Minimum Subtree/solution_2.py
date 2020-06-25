"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 不用使用全局变量
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        min_sub, min_root, min_total = self.findMin(root)
        return min_root
        
    def findMin(self, node):
        if not node:
            return float('inf'), None, 0
            
        min_left, min_left_root, min_total_left = self.findMin(node.left)
        min_right, min_right_root, min_total_right = self.findMin(node.right)
        
        total = min_total_left + min_total_right + node.val
        
        if min_left == min(min_left, min_right, total):
            return min_left, min_left_root, total
        if min_right == min(min_left, min_right, total):
            return min_right, min_right_root, total
            
        return total, node, total