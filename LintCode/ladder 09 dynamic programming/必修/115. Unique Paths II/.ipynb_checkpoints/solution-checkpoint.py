class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
            
        for j in range(m):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[n - 1][m - 1]