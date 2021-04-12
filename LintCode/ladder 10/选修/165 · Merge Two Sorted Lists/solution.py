"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        head = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next

        while l1:
            head.next = ListNode(l1.val)
            head = head.next
            l1 = l1.next

        while l2:
            head.next = ListNode(l2.val)
            head = head.next
            l2 = l2.next

        return dummy.next