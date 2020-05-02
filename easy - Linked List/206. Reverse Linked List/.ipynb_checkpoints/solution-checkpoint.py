# solution for recursion:

# https://leetcode.com/problems/reverse-linked-list/discuss/251638/Python-iterative-and-recursive-solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iteration
    def reverseList1(self, head: ListNode) -> ListNode:
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
    
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
            
        return prev
    
    # recursion with helper function
    def reverseList3(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

    # recursion without helper function
    def reverseList4(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        
        p = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return p