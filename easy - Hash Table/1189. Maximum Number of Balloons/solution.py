class Solution:
    # my solution
    def maxNumberOfBalloons(self, text: str) -> int:
        source = set('balloon')
        target = set(text)
        
        if target.intersection(source) != source:
            return 0
        
        res = []
        
        dct_text = {}
        for char in target:
            dct_text[char] = dct_text.get(char, 0) + text.count(char)
            
        tmp = {}
        for char in source:
            tmp[char] = tmp.get(char, 0) + 'balloon'.count(char)
            
        for char in source:
            res.append(dct_text[char] // tmp[char])

        return min(res)
    
    # simpler solution
    # https://leetcode.com/problems/maximum-number-of-balloons/discuss/455926/Python-easy-to-understand-solution-O(n)-time-and-O(1)-space
    def maxNumberOfBalloons(self, text: str) -> int:
        res = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
        for char in text:
            if char in res.keys():
                res[char] += 1
            
        res['l'] //= 2
        res['o'] //= 2
        
        return min(res.values())
    
    # fastest solution, faster than the above one
    def maxNumberOfBalloons(self, text: str) -> int:
        res = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
        for char in res.keys():
            res[char] = text.count(char)
            
        res['l'] //= 2
        res['o'] //= 2
        
        return min(res.values())