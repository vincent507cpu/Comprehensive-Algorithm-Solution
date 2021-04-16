class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if not s:
            return []
            
        res = []
        
        for piece in wordDict:
            if not piece:
                return []
            
            if not s.startswith(piece):
                continue
            
            if len(piece) == len(s):
                res.append(piece)
            else:
                rest = self.helper(s[len(piece):], wordDict, memo)
                
                for item in rest:
                    item = piece + ' ' + item
                    res.append(item)
                    
        memo[s] = res
        return res