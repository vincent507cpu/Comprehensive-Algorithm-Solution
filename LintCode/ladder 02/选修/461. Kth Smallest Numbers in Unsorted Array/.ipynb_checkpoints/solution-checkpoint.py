class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if right >= k:
            return self.quickSelect(nums, start, right, k)
        elif left <= k:
            return self.quickSelect(nums, left, end, k)
        else:
            return nums[k]