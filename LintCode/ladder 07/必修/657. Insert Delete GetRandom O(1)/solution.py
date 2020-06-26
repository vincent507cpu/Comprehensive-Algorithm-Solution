import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums, self.val2index = [], {}
        
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.val2index:
            return False
        
        self.nums.append(val)
        self.val2index[val] = len(self.nums) - 1
        return True
        
    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # Write your code here
        if val not in self.val2index:
            return False
        
        index = self.val2index[val]
        last = self.nums[-1]
        
        # move the last element to index
        self.nums[index] = last
        self.val2index[last] = index
        
        # remove last element
        self.nums.pop()
        del self.val2index[val]
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()