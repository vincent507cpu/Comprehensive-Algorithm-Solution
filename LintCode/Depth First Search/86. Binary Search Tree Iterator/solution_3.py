"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

'''
更简洁的代码
'''
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()
        
    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return bool(self.stack)
        
    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        node = self.stack.pop()
        nxt = node
        
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return nxt