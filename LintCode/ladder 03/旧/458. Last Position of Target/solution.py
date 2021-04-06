class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums or len(nums) == 0:
            return -1
            
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
                
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1