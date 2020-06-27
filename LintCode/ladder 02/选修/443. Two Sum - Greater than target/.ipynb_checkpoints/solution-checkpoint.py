class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        res = 0
        i, j = 0, len(nums) - 1
        
        while i < j:
            if nums[i] + nums[j] <= target:
                i += 1
            else:
                res += j - i
                j -= 1
                
        return res