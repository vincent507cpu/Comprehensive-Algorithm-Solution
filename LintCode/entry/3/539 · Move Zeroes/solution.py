class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                 r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1