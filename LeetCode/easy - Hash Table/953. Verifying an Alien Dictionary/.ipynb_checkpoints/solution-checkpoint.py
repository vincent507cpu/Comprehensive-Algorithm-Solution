# my solution

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for i in range(len(words)-1):
            if not self.compare(words[i], words[i+1], order):
                return False
            
        return True
    
    def compare(self, first, second, order):
        
        for i in range(min(len(first), len(second))):
            if order.index(first[i]) < order.index(second[i]):
                return True
            elif order.index(first[i]) > order.index(second[i]):
                return False
            
        return len(first) <= len(second)