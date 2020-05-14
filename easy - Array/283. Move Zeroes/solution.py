class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    # my ugly solution
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if nums[i] and nums[j]:
                i += 1
                j += 1
            if not nums[i] and nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] and not nums[j]:
                i += 1
                j += 1
            elif not nums[i] and not nums[j]:
                j += 1
                
    # better solutions below
    # https://leetcode.com/problems/move-zeroes/discuss/72099/Very-simple-python-solutions
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last0], nums[i] = nums[i], nums[last0]
                last0 += 1
                
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: -1 if x else 0)