class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    # two directions
    def shortestPath2(self, grid):
        # write your code here
        FORWARD_DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        BACKWARD_DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
        
        n, m = len(grid), len(grid[0])
        if not grid or not grid[0]:
            return -1
        if grid[n-1][m-1]:
            return -1
        if n * m == 1:
            return 0
        
        forward_queue = [(0, 0)]
        forward_set = set([(0, 0)])
        backward_queue = [(n - 1, m - 1)]
        backward_set = set([(n - 1, m - 1)])
        dist = 0
        
        while forward_queue and backward_queue:
            dist += 1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set, FORWARD_DIRECTIONS):
                return dist
            
            dist += 1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set, BACKWARD_DIRECTIONS):
                return dist
                
        return -1
        
    def extend_queue(self, grid, queue, visited, opposite_visited, DIRECTIONS):
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(grid, visited, new_x, new_y):
                    continue
                if (new_x, new_y) in opposite_visited:
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