# best solution

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        duplicate = sum(nums) - sum(set(nums))
        
        missing = n * (n + 1) // 2 - sum(set(nums))
        
        res = [duplicate, missing]
        
        return res