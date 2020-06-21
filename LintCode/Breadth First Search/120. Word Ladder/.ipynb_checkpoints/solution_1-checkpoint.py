class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    # single direction
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = list([start])
        visited = set([start])
        dist = 0
        
        while queue:
            dist += 1
            for i in range(len(queue)):
                word = queue.pop(0)
                if word == end:
                    return dist
                    
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
                    
        return 0
        
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words