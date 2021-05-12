class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]
        nums.sort()
        res = []
        self.dfs(nums, res, 0, [])
        return res
        
    # DFS first, then copy
    def dfs(self, nums, res, idx, subset):
        res.append(subset[:])

        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, res, i+1, subset)
            subset.pop()