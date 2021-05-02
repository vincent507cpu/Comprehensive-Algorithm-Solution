# BFS

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        zambie = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zambie.append((i, j))
                    
        res = 0
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while zambie:
            for _ in range(len(zambie)):
                x, y = zambie.pop(0)
                for dx, dy in DIRS:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                        zambie.append((new_x, new_y))
                        grid[new_x][new_y] = 1
            if zambie:
                res += 1
                
        return res if self.all_zambies(grid) else -1
        
    def all_zambies(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    return False
        return True
    
    ####################################################################################################
    def zombie(self, grid):
        # write your code here
        queue, res = [], {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # res[(i, j)] = -1
                if grid[i][j] == 1:
                    queue.append((i, j))
                    res[(i, j)] = 0

        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                    continue
                if grid[nx][ny]:
                    continue
                grid[nx][ny] = 1
                res[(nx, ny)] = res.get((x, y), 0) + 1
                queue.append((nx, ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1

        return max(res.values())