class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        if not maze:
            return -1

        queue = [start]
        # steps: minimum distance to position key from start as value.
        # e.x. steps[(3, 2)] = 2 minimum distance to location (3, 2) si 2
        # this also servers as visited.
        steps = {tuple(start):0}

        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                count = 1
                while not self.wall(nx, ny, maze):
                    nx += dx
                    ny += dy
                    count += 1
                nx -= dx
                ny -= dy
                count -= 1
                if (nx, ny) in steps: # that means the point was previously visited
                    if steps[(x, y)] + count < steps[(nx, ny)]:
                        steps[(nx, ny)] = steps[(x, y)] + count
                        queue.append((nx, ny)) # re-append to the queue if the current solution result in smallest distance
                else: # if the point was not previously visited, append to the queue
                    queue.append((nx, ny))
                    steps[(nx, ny)] = steps[(x, y)] + count

        return steps[tuple(destination)] if tuple(destination) in steps else -1

    def wall(self, x, y, maze):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return True
        
        if maze[x][y] == 1:
            return True

        return False