"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 找到小于目标值的子树，然后双指针遍历。

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root or not k:
            return []
            
        lower_stack = self.get_stack(root, target)
        upper_stack = lower_stack[:]
        
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
            
        res = []
        
        for _ in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                res.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                res.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
                
        return res
        
        
    def get_stack(self, root, target):
        stack = []
        
        while root:
            stack.append(root)
            
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return stack
        
    def move_upper(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
                
    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
            
        if not upper_stack:
            return True
            
        return target - lower_stack[-1].val < upper_stack[-1].val - target