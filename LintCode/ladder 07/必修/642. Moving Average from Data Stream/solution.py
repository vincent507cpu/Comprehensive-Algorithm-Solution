class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.lst = []
        self.total = 0
        self.count = 0
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if self.count < self.size:
            self.count += 1
            self.lst.append(val)
            self.total += val
        else:
            self.lst.append(val)
            self.total -= self.lst[0]
            self.total += val
            self.lst.pop(0)
        return self.total / self.count
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)