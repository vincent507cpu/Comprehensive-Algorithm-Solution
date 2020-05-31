class Solution:
    # my solution
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        return max(1, 1 - min(nums))
    
    # itertools.accumulate
    # https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/discuss/585562/JavaPython-3-6-and-1-liners-O(n)-Find-the-minimum-of-prefix-sum.
    def minStartValue(self, nums: List[int]) -> int:
        return 1 - min(0, min(itertools.accumulate(nums)))