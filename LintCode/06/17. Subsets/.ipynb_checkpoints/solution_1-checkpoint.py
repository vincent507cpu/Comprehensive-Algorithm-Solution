class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        self.res = []  
        
        if not nums:
            return [[]]

        nums.sort()
          
        self.dfs(nums, 0, [])
        return self.res
        
    # 递归的定义
    def dfs(self, nums, index, subset):
        # 递归的出口
        if index == len(nums):
            self.res.append(subset[:])
            return
            
        # 递归的拆解
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset)
        
        subset.pop()
        self.dfs(nums, index + 1, subset)