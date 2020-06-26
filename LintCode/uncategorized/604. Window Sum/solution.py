class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    # prefixsum
    def winSum(self, nums, k):
        # write your code here
        if not nums or k == 0:
            return []
            
        res = [sum(nums[:k])]
        
        for i in range(1, len(nums) - k + 1):
            res.append(res[-1] - nums[i - 1] + nums[i - 1 + k])
            
        return res
    
    # two pointers
    def winSum(self, nums, k):
        # write your code here
        if not nums or k == 0:
            return []
            
        res, total, j = [], 0, 0
        for i in range(len(nums)):
            while j < len(nums) and j - i < k:
                total += nums[j]
                j += 1
            if j - i == k:
                res.append(total)
            total -= nums[i]
            
        return res