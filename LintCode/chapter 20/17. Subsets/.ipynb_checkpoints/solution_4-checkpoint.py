# DFS 2

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        results = []
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, start_index, path, results):
        # if start_index == len(nums):
        results.append(path[:])
        
        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, results)
            path.pop()