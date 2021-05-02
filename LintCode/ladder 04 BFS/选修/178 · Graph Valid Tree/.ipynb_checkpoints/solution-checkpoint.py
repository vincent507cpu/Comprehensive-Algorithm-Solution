class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        if not edges:
            return True

        neighbors = {}

        for k, v in edges:
            neighbors[k] = neighbors.get(k, []) + [v]
            neighbors[v] = neighbors.get(v, []) + [k]
        
        visited, queue = {0:True}, [0]
        while queue:
            cur = queue.pop(0)
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    queue.append(node)
                    visited[cur] = True

        return len(visited) == n