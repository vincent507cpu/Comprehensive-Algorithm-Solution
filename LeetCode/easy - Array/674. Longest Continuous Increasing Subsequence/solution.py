class Solution:
    # my solution
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 1
        tmp = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                tmp += 1
            else:
                tmp = 1
            res = max(res, tmp)
            
        return res
    
    # an improved solution
    # https://leetcode.com/problems/longest-continuous-increasing-subsequence/discuss/107392/Python-Simple-Solution
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = i = 0
        while i < len(nums):
            curr = 1
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr, i = curr + 1, i + 1
            max_len = max(max_len, curr)
            i += 1
        return max_len