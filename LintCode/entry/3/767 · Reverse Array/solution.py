class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        l, r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1