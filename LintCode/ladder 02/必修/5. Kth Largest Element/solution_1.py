# quick select

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n > len(nums) or n == 0:
            return -1
            
        return self.quick_select(nums, 0, len(nums) - 1, n)
            
    def quick_select(self, nums, start, end, n):
        if start == end:
            return nums[start]
            
        pivot = nums[(start + end) // 2]
        i, j = start, end
        
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
            return self.quick_select(nums, start, j, n)
            
        if start + n - 1 >= i:
            return self.quick_select(nums, i, end, n - (i - start))
            
        return nums[j + 1]