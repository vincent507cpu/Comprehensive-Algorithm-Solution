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
        stack = []
        closest = float('inf')
        
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack[-1]
            
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            else:
                n = stack.pop()
                while stack and stack[-1].right == n:
                    n = stack.pop()
                    
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
                
        return closest