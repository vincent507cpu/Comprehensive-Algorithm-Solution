# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = []
        
        if root:
            stack.append((root.left, root.right))
            
        while stack:
            left, right = stack.pop()
            
            if left and right:
                if left.val != right.val:
                    return False
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            elif left or right:
                return False
            
        return True