# BFS 2

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        queue = [[]]
        index = 0
        
        while index < len(queue):
            subset = queue[index]
            index += 1
            
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])
            
        return queue