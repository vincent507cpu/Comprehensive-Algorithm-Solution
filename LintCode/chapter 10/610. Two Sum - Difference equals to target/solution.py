class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    # O(nlogn)
    def twoSum7(self, nums, target):
        # write your code here
        target = abs(target)
        for i in range(len(nums)):
            j = self.binary_search(nums, i + 1, len(nums) - 1, target + nums[i])
            if j != -1:
                return [nums[i], nums[j]]
                
    def binary_search(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
            
        return -1
    
    # two pointers, O(n)
    def twoSum7(self, nums, target):
        # write your code here
        target = abs(target)
        j = 1
        
        for i in range(len(nums)):
            j = max(j, i + 1)
            while j < len(nums) - 1 and nums[j] - nums[i] < target:
                j += 1
                
            if j > len(nums):
                break
            
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]