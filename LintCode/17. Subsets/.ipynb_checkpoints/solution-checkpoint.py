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
        
        for num in sorted(nums):
            for i in range(len(queue)):
                subset = list(queue[i])
                subset.append(num)
                queue.append(subset)
                
        return queue