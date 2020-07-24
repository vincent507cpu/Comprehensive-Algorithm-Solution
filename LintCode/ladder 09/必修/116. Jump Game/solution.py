class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        dp = [False] * len(A)
        dp[0] = True
        
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and A[j] + j >= i:
                    dp[i] = True
                    break
                
        return dp[-1]