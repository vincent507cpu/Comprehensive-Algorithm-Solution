class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return
        
        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i != 0:
            j = n - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
        self.swapList(nums, i, n-1)