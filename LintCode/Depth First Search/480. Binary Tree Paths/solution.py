"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    # first verion of DFS
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
            
        if not root.left and not root.right:
            return [str(root.val)]
            
        paths = []
        
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        
        for path in leftPath + rightPath:
            paths.append(str(root.val) + '->' + path)
            
        return paths
    
    # second version of DFS
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
            
        res = []
        self.findPaths(root, [str(root.val)], res)
        
        return res
        
    def findPaths(self, root, path, res):
        if not root.left and not root.right:
            res.append('->'.join(path))
            return
            
        if root.left:
            path.append(str(root.left.val))
            self.findPaths(root.left, path, res)
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.findPaths(root.right, path, res)
            path.pop()