# https://www.jianshu.com/p/2fd4c45cab25

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not (grid and grid[0]):
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0

        DIR = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        queue, visited, distance = [(source.x, source.y)], set(), {}
        distance[(source.x, source.y)] = 0

        while queue:
            x, y = queue.pop(0)
            
            if (x, y) == (destination.x, destination.y):
                    return distance[(x, y)]

            for dx, dy in DIR:
                if (0 > x+dx or x+dx >= len(grid)) or (0 > y+dy or y+dy >= len(grid[0])):
                    continue
                if grid[x+dx][y+dy]:
                    continue
                if (x+dx, y+dy) in visited:
                    continue
                queue.append((x+dx, y+dy))
                visited.add((x+dx, y+dy))
                distance[(x+dx, y+dy)] = distance[(x, y)] + 1

        return -1