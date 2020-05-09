class Solution:
    # brutal force
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        
        text = text.split()
        
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
                
        return res
    
    # two hashes, fastest algorithm
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        word_idx = {}
        idx_word = {}
        text = text.split()

        for i, w in enumerate(text):
            word_idx[w] = word_idx.get(w, []) + [i]
            idx_word[i] = w

        for idx in word_idx[first]:
            if idx+1 in word_idx[second] and idx < len(text) - 2:
                res.append(idx_word[idx+2])

        return res
    
    # list comprhension
    # https://leetcode.com/problems/occurrences-after-bigram/discuss/562161/Python3-Easy-Two-Liner
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()

        return [text[i] for i in range(2, len(text)) if text[i-2] == first and text[i-1] == second]