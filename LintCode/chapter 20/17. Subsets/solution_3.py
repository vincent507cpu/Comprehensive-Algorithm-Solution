# DFS 1

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
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, path, results):
        if index == len(nums):
            results.append(path[:])
            return
        
        path.append(nums[index])
        self.dfs(nums, index + 1, path, results)
        path.pop()
        
        self.dfs(nums, index + 1, path, results)