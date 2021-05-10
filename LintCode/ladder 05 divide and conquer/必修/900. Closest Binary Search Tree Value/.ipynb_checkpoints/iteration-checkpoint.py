"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        res = float('inf')
        val = None

        while root:
            if root.val == target:
                return root.val
            elif root.val < target:
                if res > abs(root.val - target):
                    res = abs(root.val - target)
                    val = root.val
                root = root.right
            else:
                if res > abs(root.val - target):
                    res = abs(root.val - target)
                    val = root.val
                root = root.left

        return val