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
    @return: An integer
    """
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34216/Simple-solution-using-Java
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
            
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1