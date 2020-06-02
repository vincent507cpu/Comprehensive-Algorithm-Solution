class Solution:
    # hash map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        
        for i, n in enumerate(nums):            
            if n not in dct:
                dct[target - n] = i
            else:
                return [dct[n], i]
            
    # to pointers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = [(num, idx) for idx, num in enumerate(nums)]
        new.sort()
        
        l, r = 0, len(new) - 1
        while l < r:
            if new[l][0] + new[r][0] > target:
                r -= 1
            elif new[l][0] + new[r][0] < target:
                l += 1
            else:
                return [new[l][1], new[r][1]]