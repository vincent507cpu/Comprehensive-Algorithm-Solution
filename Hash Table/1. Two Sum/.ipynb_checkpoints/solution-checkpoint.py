class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        
        for i, n in enumerate(nums):            
            if n not in dct:
                dct[target - n] = i
            else:
                return [dct[n], i]