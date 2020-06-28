
                
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        res, visited = 0, set([start])
        queue = [start]
        
        while queue:
            res += 1
            
            for _ in range(len(queue)):
                cur = queue.pop(0)

                if cur == end:
                    return res
                    
                for next_word in self.get_next(cur):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
                    
        return -1
                    
    def get_next(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                if word[i] == char:
                    continue
                
                words.append(left + char + right)
                
        return words