# optumal soltuion - state compressing DP

class Result:
    def __init__(self):
        self.min_cost = float('inf')

class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        # Write your code here
        graph = self.construcGraph(roads, n)
        state_size = 1 << n
        f = [[float('inf')] * (n + 1) for _ in range(state_size)]
        f[1][1] = 0
        
        for state in range(state_size):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)) == 0:
                    continue
                prev_state = state ^ (1 << (i - 1))
                
                for j in range(1, n + 1):
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    f[state][i] = min(f[state][i], f[prev_state][j] + graph[j][i])
            
        return min(f[state_size - 1])
        
    def construcGraph(self, roads, n):
        graph = {
            i : {j: float('inf') for j in range(1, n + 1)} \
            for i in range(1, n + 1)
        }
        
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
            
        return graph