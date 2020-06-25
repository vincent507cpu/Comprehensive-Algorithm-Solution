# my solution, should be the best one

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1
                
        return n