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
        
        head = root
        prev = cur = None
        
        while head:
            if not prev:
                prev = head.left or head.right
            
            if head.left:
                if cur:
                    cur.next = head.left
                cur = head.left
                
            if head.right:
                if cur:
                    cur.next = head.right
                cur = head.right
                
            if head.next:
                head = head.next
            else:
                head = prev
                cur = prev = None
                
        return root