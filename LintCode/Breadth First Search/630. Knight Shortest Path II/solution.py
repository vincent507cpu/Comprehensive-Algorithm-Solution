class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        # 位移方向为什么取相反数？
        DIRECTIONS = [
            (1, -2),
            (-1, -2),
            (2, -1),
            (-2, -1)]
            
        n, m = len(grid), len(grid[0])
        
        step = [[float('inf') for _ in range(m)] for _ in range(n)]
        step[0][0] = 0
        
        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                
                # 这个循环不明白
                for delta_x, delta_y in DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        step[i][j] = min(step[i][j], step[x][y] + 1)
                        
        if step[n - 1][m - 1] == float('inf'):
            return -1
            
        return step[n - 1][m - 1]