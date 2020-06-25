class Solution:
    # my solution
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(0, len(nums)-1, 2):
            res += min(nums[i:i+2])
            
        return res
    
    # more concise solution
    # https://leetcode.com/problems/array-partition-i/discuss/102161/Python-1-line-(sorting-is-accepted)
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])