class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        dct = {}
        res, last_res = 0, []
        
        for i in range(len(nums)):
            if i and nums[i - 1] == nums[i] and nums[i] + nums[i - 1] != target:
                continue
            
            if target - nums[i] not in dct:
                dct[nums[i]] = target - nums[i]
            else:
                if [target - nums[i], nums[i]] == last_res:
                    continue
                res += 1
                last_res = [target - nums[i], nums[i]]
                
        return res