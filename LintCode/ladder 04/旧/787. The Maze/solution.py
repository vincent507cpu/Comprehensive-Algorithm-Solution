class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = [start]
        while queue:
            x, y = queue.pop(0)
            maze[x][y] = 2
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                while 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != 1:
                    new_x += dx
                    new_y += dy
                new_x -= dx
                new_y -= dy
                if maze[new_x][new_y] == 0:
                    queue.append((new_x, new_y))

        return False