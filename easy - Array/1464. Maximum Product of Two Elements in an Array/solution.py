class Solution:
    # sort array, the last 2 elements are the biggest ones
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return (nums[-1] - 1) * (nums[-2] - 1)