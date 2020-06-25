# best solution
# https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        
        for i, num in enumerate(nums):
            if num in dct and i - dct[num] <= k:
                return True
            dic[num] = i
            
        return False