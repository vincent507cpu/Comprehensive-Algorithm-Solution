class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        queue = [start]

        while queue:
            x, y = queue.pop(0)
            if [x, y] == destination:
                return True

            maze[x][y] = 2

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if not maze[nx][ny]:
                    queue.append([nx, ny])

        return False