class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        left = self.findBoundaries(nums, target)
        if left == -1:
            return [-1, -1]
            
        right = self.findBoundaries(nums, target, findLeft=False)
        
        return [left, right]
        
    def findBoundaries(self, nums, target, findLeft=True):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                if findLeft:
                    end = mid
                else:
                    start = mid
                        
        if findLeft:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
        else:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
                
        return -1