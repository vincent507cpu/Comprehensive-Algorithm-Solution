# my solution

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, tmp = 0, 0
        
        for n in nums:
            if n == 1:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 0
                
        return res
    
    # another solution
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)