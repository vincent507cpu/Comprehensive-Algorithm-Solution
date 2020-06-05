class Solution:
    # iteration
    def majorityElement(self, nums: List[int]) -> int:
        dct, n = {}, len(nums)
        
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] > n / 2:
                return num
            
    # https://leetcode.com/problems/majority-element/discuss/51610/One-line-solution-in-Python
    # NOTICE that the majority element always exist in the array,so that the middle always is the answer
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]