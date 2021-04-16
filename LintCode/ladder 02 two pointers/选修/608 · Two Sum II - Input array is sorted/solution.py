# two pointers

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] + nums[right] < target:
                left += 1
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            if left < right and nums[left] + nums[right] == target:
                return [left+1, right+1]