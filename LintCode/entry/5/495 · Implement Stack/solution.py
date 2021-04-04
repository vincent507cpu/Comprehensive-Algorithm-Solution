class Stack:
    def __init__(self):
        self.lst = []
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.lst.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        return self.lst.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.lst[-1]
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not bool(self.lst)