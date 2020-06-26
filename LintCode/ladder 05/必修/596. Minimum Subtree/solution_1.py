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
        if not root:
            return
        
        self.minimum = float('inf')
        self.min_root = None
        self.get_min_subtree(root)
        
        return self.min_root
        
    def get_min_subtree(self, node):
        if not node:
            return 0
            
        min_left = self.get_min_subtree(node.left)
        min_right = self.get_min_subtree(node.right)
        weight = min_left + min_right + node.val
        
        if weight < self.minimum:
            self.minimum = weight
            self.min_root = node
            
        return weight