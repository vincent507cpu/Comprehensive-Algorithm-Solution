"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        cur = root
        prevChild = curChild = None
        
        while cur:
            if not curChild:
                curChild = cur.left or cur.right
                
            if cur.left:
                if prevChild:
                    prevChild.next = cur.left
                prevChild = cur.left
                
            if cur.right:
                if prevChild:
                    prevChild.next = cur.right
                prevChild = cur.right
                
            if cur.next:
                cur = cur.next
            else:
                cur = curChild
                prevChild = curChild = None
                
        return root