class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1:
            return nums
            
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
            
        if i != 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            
        self.swap(nums, i, n - 1)
        
        return nums
        
    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1