class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    # bidriectional
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1
            
        dict.add(start)
        dict.add(end)
        graph = self.construct_graph(dict)
        
        forward_queue = [start]
        forward_set = set([start])
        backward_queue = [end]
        backward_set = set([end])
        
        dist = 1
        while forward_queue and backward_queue:
            dist += 1
            if self.extend_queue(graph, forward_queue, forward_set, backward_set):
                return dist
                
            dist += 1
            if self.extend_queue(graph, backward_queue, backward_set, forward_set):
                return dist
                
        return -1
        
    def extend_queue(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            word = queue.pop(0)
            for next_word in graph[word]:
                if next_word in visited:
                    continue
                if next_word in opposite_visited:
                    return True
                queue.append(next_word)
                visited.add(next_word)
        return False
        
    def construct_graph(self, word_set):
        graph = {}
        for word in word_set:
            graph[word] =  self.get_next_word(word, word_set)
        return graph
        
    def get_next_word(self, word, word_set):
        next_word_set = set()
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            chars = list('qwertyuiopasdfghjklzxcvbnm')
            chars.remove(word[i])
            
            for char in chars:
                next_word = left + char + right
                if next_word in word_set:
                    next_word_set.add(next_word)
                    
        return next_word_set