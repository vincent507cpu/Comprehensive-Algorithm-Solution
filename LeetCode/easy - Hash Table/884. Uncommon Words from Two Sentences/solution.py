# concise solution
# https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/314449/Python3-100-Faster

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = []
        words = A.split() + B.split()
        
        for word in words:
            if words.count(word) == 1:
                res.append(word)
                
        return res