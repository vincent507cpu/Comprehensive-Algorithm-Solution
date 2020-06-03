class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1]:
                left = mid
            else:
                right = mid
                
        return max(nums[left], nums[right])