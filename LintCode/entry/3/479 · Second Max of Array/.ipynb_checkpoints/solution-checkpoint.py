class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        first, second = float('-inf'), float('-inf')

        for num in nums:
            if num >= first:
                second = first
                first = num
            elif num > second:
                second = num

        return second