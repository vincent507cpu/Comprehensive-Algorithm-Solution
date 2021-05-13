class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    if [nums[i], nums[left], nums[right]] in res:
                        left += 1
                        continue
                    
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
        return res