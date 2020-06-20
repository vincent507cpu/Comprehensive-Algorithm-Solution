class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org
        
    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
                    
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
                
        return graph
        
    def get_inDegrees(self, graph):
        inDegree = {node: 0 for node in graph}
        
        for node in graph:
            for neighbor in graph[node]:
                inDegree[neighbor] += 1
                
        return inDegree
        
    def topological_sort(self, graph):
        inDegree = self.get_inDegrees(graph)
        
        queue = []
        for node in graph:
            if inDegree[node] == 0:
                queue.append(node)
                
        topo_order = []
        while queue:
            if len(queue) > 1:
                return None
                
            node = queue.pop(0)
            topo_order.append(node)
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
        
        return None