"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        in_degrees = self.get_in_degrees(graph)
        queue = [node for node, neighbors in in_degrees.items() if neighbors == 0]
        res = []
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            
            for neighbor in node.neighbors:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res
        
    def get_in_degrees(self, graph):
        in_degrees = {node: 0 for node in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                in_degrees[neighbor] += 1
                
        return in_degrees