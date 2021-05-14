# https://github.com/lilianweng/LeetcodePython/blob/master/next_permutation.py

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        i = len(nums) - 2
        
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            return nums.sort()
        
        j = len(nums) - 1
        while nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        
        return nums