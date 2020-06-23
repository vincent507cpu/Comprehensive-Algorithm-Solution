"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# inorder iteration

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        
        if not root:
            return res
            
        dummy = TreeNode(float('inf'))
        dummy.right = root
        stack = [dummy]
        
        while stack:
            node = stack.pop()
            if k1 <= node.val and node.val <= k2:
                res.append(node.val)

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
                    
        return res