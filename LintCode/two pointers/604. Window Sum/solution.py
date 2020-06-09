class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums or k == 0:
            return []
            
        res = [sum(nums[:k])]
        
        for i in range(1, len(nums) - k + 1):
            res.append(res[-1] - nums[i - 1] + nums[i - 1 + k])
            
        return res