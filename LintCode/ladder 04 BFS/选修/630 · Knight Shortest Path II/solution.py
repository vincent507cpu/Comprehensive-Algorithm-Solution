

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        distance = {(0, 0):0}
        row, col = len(grid), len(grid[0])
        DIR = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        visited = {(0, 0)}
        queue = [(0, 0)]

        while queue:
            x, y = queue.pop(0)
            if x == row - 1 and y == col - 1:
                return distance[(x, y)]

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < row and ny < col):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny]:
                    continue
                
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited.add((nx, ny))

        return -1