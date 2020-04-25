# best solution:

# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tmp = dummy
        
        while l1 and l2:
            dummy.next = ListNode(min(l1.val, l2.val))
            dummy = dummy.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
                
        dummy.next = l1 or l2
#         dummy.next = l1 if l1 else l2
        
        return tmp.next