# 从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。 然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, distance, dict)
        
        result = []
        self.dfs(start, end, distance, dict, [start], result)
        
        return result
        
    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = [start]
        
        while queue:
            word = queue.pop(0)
            
            for next_word in self.get_next_word(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
                    
    def get_next_word(self, word, dict):
        words = []
        
        for i in range(len(word)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                next_word = word[:i] + char + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
                    
        return words
        
    def dfs(self, current, target, distance, dict, path, result):
        if current == target:
            result.append(path[:])
            return
        
        for word in self.get_next_word(current, dict):
            if distance[word] != distance[current] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, result)
            path.pop()