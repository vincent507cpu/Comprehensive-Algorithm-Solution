"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root:
            return None
        
        self.maxVal = float('-inf')
        self.res = None
        
        self.findMax(root)
            
        return self.res
        
    def findMax(self, node):
        if not node:
            return 0
        
        leftSum = self.findMax(node.left)
        rightSum = self.findMax(node.right)
        
        if leftSum + rightSum + node.val > self.maxVal or not self.res:
            self.maxVal = leftSum + rightSum + node.val
            self.res = node
            
        return leftSum + rightSum + node.val