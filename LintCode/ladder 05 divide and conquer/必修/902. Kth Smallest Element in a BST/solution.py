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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        queue = [dummy]
        
        for _ in range(k):
            node = queue.pop()
            if node.right:
                node = node.right
                while node:
                    queue.append(node)
                    node = node.left
            if not queue:
                return None
                
        return queue[-1].val