class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # my solution
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
            
        return False
    
    # more concise solution
    # https://leetcode.com/problems/contains-duplicate/discuss/61076/In-python-this-problem-is-a-joke
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))