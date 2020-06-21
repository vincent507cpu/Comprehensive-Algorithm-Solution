class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        dct = {}
        length = len(nums)
        
        for n in nums:
            dct[n] = dct.get(n, 0) + 1
            if dct[n] / length > 1 / k:
                return n