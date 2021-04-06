class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        left, index, right = 0, 0, len(nums) - 1
        
        while index <= right:
            if low <= nums[index] <= high:
                index += 1
            elif nums[index] < low:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1