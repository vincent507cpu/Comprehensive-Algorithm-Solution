class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        i, j = 0, 1
        
        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
                
            while i < j and nums[i] != 0:
                i += 1
                
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                
        return nums