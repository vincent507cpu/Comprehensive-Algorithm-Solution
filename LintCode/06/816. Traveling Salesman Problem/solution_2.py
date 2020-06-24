# brutal DFS + pruning

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
        result = Result()
        self.dfs(1, n, [1], set([1]), 0, graph, result)
        return result.min_cost
        
    def construcGraph(self, roads, n):
        graph = {
            i : {j: float('inf') for j in range(1, n + 1)} \
            for i in range(1, n + 1)
        }
        
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
            
        return graph
        
    def dfs(self, city, n, path, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return
        
        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue
            
            visited.add(next_city)
            path.append(next_city)
            self.dfs(next_city, n, path, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)
            path.pop()
            
    def has_better_path(self, graph, path, city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] > \
            graph[path[i - 1]][path[-1]] + graph[path[i]][city]:
                return True
                
        return False