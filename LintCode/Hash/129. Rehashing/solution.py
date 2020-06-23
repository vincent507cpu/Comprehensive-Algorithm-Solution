"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        HASH_SIZE = len(hashTable) * 2
        res = [None for _ in range(HASH_SIZE)]
        
        for item in hashTable:
            # p = item
            while item != None:
                self.addNode(res, item.val)
                item = item.next
                
        return res
        
    def addNode(self, table, number):
        p = number % len(table)
        
        if table[p] == None:
            table[p] = ListNode(number)
        else:
            self.addListNode(table[p], number)
            
    def addListNode(self, node, number):
        if node.next != None:
            self.addListNode(node.next, number)
        else:
            node.next = ListNode(number)