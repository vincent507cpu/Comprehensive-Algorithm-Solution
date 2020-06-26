class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyQueue:
    def __init__(self):
        self.head, self.tail = None, None
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        value = self.head.val
        self.head = self.head.next
        
        return value