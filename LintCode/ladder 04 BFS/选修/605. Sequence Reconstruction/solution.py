class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.construct_graph(seqs)
        topo = self.topo_sort(graph)
        return topo == org

    def construct_graph(self, seqs):
        graph = {}

        for seq in seqs:
            for n in seq:
                if n not in graph:
                    graph[n] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph
    
    def build_in_degree(self, graph):
        in_degree = {n:0 for n in graph}

        for node in graph:
            for n in graph[node]:
                in_degree[n] += 1

        return in_degree

    def topo_sort(self, graph):
        topo = []
        in_degree = self.build_in_degree(graph)
        queue = [key for key, val in in_degree.items() if not val]

        while queue:
            if len(queue) > 1:
                return None

            node = queue.pop(0)
            topo.append(node)

            for val in graph[node]:
                in_degree[val] -= 1
                if in_degree[val] == 0:
                    queue.append(val)

        return topo if len(topo) == len(in_degree) else None