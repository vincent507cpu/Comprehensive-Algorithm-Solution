"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
# two directions search
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        if not grid or not grid[0]:
            return -1
        if grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        
        forwad_queue = [(source.x, source.y)]
        forwad_set = set([(source.x, source.y)])
        backward_queue = [(destination.x, destination.y)]
        backward_set = set([(destination.x, destination.y)])
        dist = 0
        
        while forwad_queue and backward_queue:
            dist += 1
            if self.extend_queue(grid, forwad_queue, forwad_set, backward_set, DIRECTIONS):
                return dist
            
            dist += 1
            if self.extend_queue(grid, backward_queue, backward_set, forwad_set, DIRECTIONS):
                return dist
            
        return -1
        
    def extend_queue(self, grid, queue, visited, opposite, DIRECTIONS):
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(grid, visited, new_x, new_y):
                    continue
                if (new_x, new_y) in opposite:
                    return True
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        return False
        
    def is_valid(self, grid, visited, x, y):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        return (x, y) not in visited