class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not len(grid[0]):
            return 0
            
        res = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    res += 1
                    
        return res
        
    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = [(x, y)]
        visited.add((x, y))
        
        while queue:
            x, y = queue.pop(0)
            
            for delta_x, delta_y in DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                
    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
            
        return grid[x][y]