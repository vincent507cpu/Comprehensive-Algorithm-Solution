class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        n, m = len(map), len(map[0])
        
        if not m or not n:
            return False
            
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        lst = [0]
        
        while lst:
            cur = lst.pop(0)
            cur_x = cur // m
            cur_y = cur % m
            
            for i in range(4):
                n_x = cur_x + dx[i]
                n_y = cur_y + dy[i]
                
                if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m or visited[n_x][n_y] or map[n_x][n_y] == 0: 
                    # 检查是否越界、是否已经访问过以及能否通过
                        continue
                    
                if map[n_x][n_y] == 9:
                    return True
                    
                lst.append(n_x * m + n_y)
                visited[n_x][n_y] = True
                
        return False