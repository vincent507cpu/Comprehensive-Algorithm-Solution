class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        res = float('inf')
        i, j = 0, len(nums) - 1
        
        while i < j:
            if nums[i] + nums[j] < target:
                res = min(res, abs(target - (nums[i] + nums[j])))
                i += 1
            elif nums[i] + nums[j] > target:
                res = min(res, abs(target - (nums[i] + nums[j])))
                j -= 1
            else:
                return 0
                
        return res