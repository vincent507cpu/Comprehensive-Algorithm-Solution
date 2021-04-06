class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        i, j = 0, 1
        target = abs(target)
        
        for i in range(len(nums)):
            j = max(j, i + 1)
            
            while j < len(nums) - 1 and nums[j] - nums[i] < target:
                j += 1
                
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]