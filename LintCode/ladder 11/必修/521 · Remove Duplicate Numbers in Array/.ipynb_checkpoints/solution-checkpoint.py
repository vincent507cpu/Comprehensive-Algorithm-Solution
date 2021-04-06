class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        idx, right = 0, 1

        for i in range(len(nums)):
            while right < len(nums) and nums[i] == nums[right]:
                right += 1

            idx = i

            if right == len(nums):
                break

            nums[i+1] = nums[right]

        return idx + 1