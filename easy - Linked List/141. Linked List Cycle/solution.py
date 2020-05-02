# best solution:

# https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow, fast = head, head.next
            
            while slow.val != fast.val:
                slow = slow.next
                fast = fast.next.next
            
            return True
        except:
            return False