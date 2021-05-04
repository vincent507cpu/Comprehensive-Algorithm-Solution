"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        if not s or not t:
            return -1
        if s == t:
            return 0
            
        res, visited = 0, set()

        queue = [s]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                for neighbor in node.neighbors:
                    if neighbor == t:
                        return res + 1
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            res += 1

        return -1