class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        nums.sort()
        i = 0
        while i < len(nums):
            if i != nums[i]:
                return i
            i += 1
        return len(nums)