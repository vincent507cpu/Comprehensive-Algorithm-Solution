class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        res, l, r = 0, 0, len(nums) - 1
        nums.sort()
        
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += r - l
                l += 1
                
        return res