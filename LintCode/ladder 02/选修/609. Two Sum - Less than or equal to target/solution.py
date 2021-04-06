class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return 0
            
        nums.sort()
        
        left, right, res = 0, len(nums) - 1, 0
        
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += right - left
                left += 1
                
        return res