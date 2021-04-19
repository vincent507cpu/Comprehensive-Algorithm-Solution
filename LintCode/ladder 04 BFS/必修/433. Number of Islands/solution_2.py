class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        res, queue, visited = 0, [], set()
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not queue and (i, j) not in visited:
                    res += 1
                    queue.append((i, j))

                while queue:
                    x, y = queue.pop(0)

                    for dx, dy in DIR:
                        nx = x + dx
                        ny = y + dy
                        if not (0 <= nx < len(grid)\
                                and 0 <= ny < len(grid[0])):
                            continue
                        if not grid[nx][ny]:
                            continue
                        if (nx, ny) in visited:
                            continue
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        return res