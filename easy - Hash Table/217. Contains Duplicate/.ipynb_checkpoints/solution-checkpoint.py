class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        res = set()
        
        for n in nums:
            if n not in res:
                res.add(n)
            else:
                return True
            
        return False
    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
            
        return False