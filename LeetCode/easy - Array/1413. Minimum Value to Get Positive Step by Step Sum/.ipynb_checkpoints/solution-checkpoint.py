class Solution:
    # my solution
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        return 1 - min(nums) if 1 - min(nums) > 0 else 1
    
    # itertools.accumulate
    # https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/discuss/585576/Python-One-Liner-using-Prefix-Sum-with-explanation
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, max(1 - i for i in itertools.accumulate(nums)))