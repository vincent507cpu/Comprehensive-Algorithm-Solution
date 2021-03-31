"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        # dummy = ListNode(0, next=head)
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow