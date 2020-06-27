"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
            
        res = set()
        queue = [root]
        
        while queue:
            node = queue.pop(0)

            if n - node.val not in res:
                res.add(node.val)
            else:
                return [node.val, n - node.val]
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return None