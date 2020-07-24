class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[target]