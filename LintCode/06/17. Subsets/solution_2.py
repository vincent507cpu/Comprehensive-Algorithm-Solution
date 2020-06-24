class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        
        if not nums:
            return [[]]
            
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    # DFS first, then copy
    def dfs(self, nums, startIdx, result, res):
        res.append(result[:])
            
        for i in range(startIdx, len(nums)):
            result.append(nums[i])
            self.dfs(nums, i + 1, result, res)
            result.pop()
            
    # copy first, then DFS
    def dfs(self, nums, startIdx, result, res):
        res.append(result)
            
        for i in range(startIdx, len(nums)):
            new = result[:]
            new.append(nums[i])
            self.dfs(nums, i + 1, new, res)