"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    # https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
            
        l = self.depth(root.left)
        r = self.depth(root.right)
        
        return abs(l - r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, node):
        if not node:
            return 0
            
        return max(self.depth(node.left), self.depth(node.right)) + 1