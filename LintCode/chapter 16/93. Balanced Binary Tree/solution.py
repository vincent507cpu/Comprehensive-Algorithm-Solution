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
    @return: True if the binary tree is BST, or false
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.check_balance(root)
        return is_balanced
        
    def check_balance(self, root):
        if not root:
            return True, 0
            
        is_left_balanced, left_depth = self.check_balance(root.left)
        is_right_balanced, right_depth = self.check_balance(root.right)
        root_dapth = max(left_depth, right_depth) + 1
        
        if not is_left_balanced or not is_right_balanced:
            return False, root_dapth
        if abs(left_depth - right_depth) > 1:
            return False, root_dapth
        return True, root_dapth