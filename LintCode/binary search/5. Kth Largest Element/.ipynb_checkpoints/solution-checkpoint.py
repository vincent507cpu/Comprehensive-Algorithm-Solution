class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n > len(nums) or len(nums) == 0:
            return -1
            
        return self.qucikSelect(n, nums, 0, len(nums) - 1)
        
    def qucikSelect(self, n, nums, start, end):
        if start == end:
            return nums[start]
            
        i, j = start, end
        pivot = nums[(i + j) // 2]
        
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
                
            while i <= j and nums[j] < pivot:
                j -= 1
                
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        if start + n - 1 <= j:
            return self.qucikSelect(n, nums, start, j)
            
        if start + n - 1 >= i:
            return self.qucikSelect(n - (i - start), nums, i, end)
            
        return nums[j + 1]