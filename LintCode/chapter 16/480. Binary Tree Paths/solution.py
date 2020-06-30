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
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
            
        paths = []
        self.find_path(root, [str(root.val)], paths)

        return paths
        
    def find_path(self, node, path, paths):
        if not node.left and not node.right:
            paths.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.find_path(node.left, path, paths)
            path.pop()
        
        if node.right:
            path.append(str(node.right.val))
            self.find_path(node.right, path, paths)
            path.pop()