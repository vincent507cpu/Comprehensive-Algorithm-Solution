"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
# one direction search
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
            
        DIRECTION = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
        
        queue = [(source.x, source.y)]
        distance = {(source.x, source.y): 0}
        
        while queue:
            x, y = queue.pop(0)
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTION:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in distance:
                    continue
                if not self.is_valid(new_x, new_y, grid):
                    continue
                distance[(new_x, new_y)] = distance[(x, y)] + 1
                queue.append((new_x, new_y))
        return -1
            
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
            
        return not grid[x][y]    