# binary search + greedy

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
            
        lst = [float('inf')] * (len(nums) + 1)
        lst[0] = float('-inf')
        
        res = 0
        for i in range(len(nums)):
            index = self.first_gte(lst, nums[i])
            lst[index] = nums[i]
            res = max(res, index)
            
        return res
        
    def first_gte(self, lst, n):
        start, end = 0, len(lst) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if lst[mid] >= n:
                end = mid
            else:
                start = mid
                
        if lst[start] >= n:
            return start
        return end