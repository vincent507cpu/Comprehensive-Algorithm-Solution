# buttom-up

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1
            
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                
        return dp[0][0]