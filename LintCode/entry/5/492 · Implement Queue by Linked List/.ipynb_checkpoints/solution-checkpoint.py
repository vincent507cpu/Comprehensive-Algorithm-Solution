class MyQueue:
    def __init__(self):
        self.stack = []
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        self.stack.append(item)
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        return self.stack.pop(0)