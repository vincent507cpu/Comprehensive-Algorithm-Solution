# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) space complexity
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        return lst == lst[::-1]
    
    # O(1) space complexity
    # https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
    def isPalindrome(self, head):
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next

            # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
           # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False 
        return not rev