class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        i, j = 0, 0
        res, tmp = [], 0
        
        while j < len(nums):
            while j - i < k:
                tmp += nums[j]
                j += 1
                
            res.append(tmp)
            tmp -= nums[i]
            i += 1
            
