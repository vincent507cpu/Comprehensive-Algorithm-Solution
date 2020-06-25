# best solution
# https://leetcode.com/problems/keyboard-row/discuss/97881/Solution-in-python-using-set

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        
        for word in words:    
            w = set(word.lower())
            if w & a == w or w & b == w or w & c == w:
                res.append(word)
                
        return res