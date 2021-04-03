class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        
        if len(nums) == 1:
            return nums[0]

        count = dict()

        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] > len(nums) / 2:
                return i