class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    # tow pointers
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
            
        nums.sort()
        idx, j = 0, 1
        
        for i in range(len(nums)):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
                
            idx = i
            
            if j == len(nums):
                break
            
            nums[i + 1] = nums[j]
            
        return idx + 1