class Solution:
    # my solution
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        left, right = 0, sum(nums[1:])
        if left == right:
            return 0
        
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
            
        return -1
    
    # a slightly better solution
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
            
        return -1