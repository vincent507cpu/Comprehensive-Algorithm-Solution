class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        self.res = []
        nums.sort()
        self.dfs(nums, 0, [], self.res)
        return self.res
        
    def dfs(self, nums, startIdx, subset, res):
        res.append(subset[:])

        for i in range(startIdx, len(nums)):
            if i and nums[i] == nums[i - 1] and i > startIdx:
                continue
            
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            subset.pop()