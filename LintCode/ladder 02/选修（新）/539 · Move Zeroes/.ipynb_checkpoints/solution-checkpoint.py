# two pointers in same direction

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0

        while right < len(nums):
            if not nums[right]:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1