# BFS with sub-functions

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
            
        root = node
        nodes = self.get_nodes(node)
        
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return mapping[root]
        
    def get_nodes(self, node):
        queue = [node]
        result = set([node])
        while queue:
            head = queue.pop(0)
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        
        return result