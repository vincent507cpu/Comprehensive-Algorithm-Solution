class Solution:
    # my initial solution
    def countCharacters(self, words: List[str], chars: str) -> int:
        def count(word):
            word = list(word)
            dct = {}
            for char in word:
                dct[char] = dct.get(char, 0) + 1
            return dct
        
        chars = count(chars)
        res = 0
        for word in words:
            tmp = count(word)
            flag = True
            while flag:
                for char in tmp.keys():
                    if char not in chars.keys():
                        flag = False
                    elif tmp[char] > chars[char]:
                        flag = False
                break
                        
            if flag:
                res += len(word)
                
        return res
    
    # faster solution
    # consulted https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/365638/python-3-simple-solution
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for word in words:
            flag = True
            for char in word:
                if word.count(char) > chars.count(char):
                    flag = False
                    break
                                
            if flag:
                res += len(word) 
                    
        return res