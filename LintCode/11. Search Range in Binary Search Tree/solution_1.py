"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# BFS

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
            
        res, queue = [], [root]
        
        index = 0
        
        while index < len(queue):
            if queue[index]:
                if queue[index].val >= k1 and queue[index].val <= k2:
                    res.append(queue[index].val)
                    
                queue.append(queue[index].left)
                queue.append(queue[index].right)
                
            index += 1
            
        return sorted(res)