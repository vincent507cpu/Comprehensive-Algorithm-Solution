class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
                
            mid = (start + end) // 2
        
            if nums[start] > nums[mid]:
                end = mid
            elif nums[start] < nums[mid]:
                start = mid
            else:
                start += 1
                
        return nums[start]