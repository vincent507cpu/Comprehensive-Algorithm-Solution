class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        queue = [(0, 0)]
        
        while queue:
            x, y = queue.pop()
            if map[x][y] == 9:
                return True
            if self.is_valid(map, x + 1, y):
                queue.append((x + 1, y))
            if self.is_valid(map, x, y + 1):
                queue.append((x, y + 1))
                
        return False
        
    def is_valid(self, map, x, y):
        if x == len(map[0]):
            return False
        if y == len(map):
            return False
            
        return bool(map[x][y])