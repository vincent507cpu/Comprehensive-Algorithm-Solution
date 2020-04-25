# best solution:

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28621/Simple-iterative-Python-6-lines-60-ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        
        # while loop already check the edge cases
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
                
        return dummy.next