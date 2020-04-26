# solution for recursion:

# https://leetcode.com/problems/reverse-linked-list/discuss/251638/Python-iterative-and-recursive-solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iteration
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        pre = ListNode(head.val)
        cur = head.next
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        return pre
    
    # recursion
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p