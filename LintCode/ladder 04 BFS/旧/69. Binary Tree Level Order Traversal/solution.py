"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    # single layer queue
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = collections.deque([root])
        res = []
        
        while queue:
            res.append([node.val for node in queue])
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res
    
    # double layers queue
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = collections.deque([root])
        res = []
        
        while queue:
            res.append([node.val for node in queue])
            next_queue = []
            
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                    
            queue = next_queue
            
        return res
    
    # dummy node
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = collections.deque([root, None])
        res, level = [], []
        
        while queue:
            node = queue.popleft()
            
            if not node:
                res.append(level)
                level = []
                
                if queue:
                    queue.append(None)
                continue
            
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return res