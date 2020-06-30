# DFS

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        res = []
        self.dfs(s, dict, [], res)
        return bool(res)
        
    def dfs(self, s, dict, subset, res):
        if s == '':
            res.append(subset)
            return
        
        for piece in dict:
            if not s.startswith(piece):
                continue
            
            subset.append(piece)
            self.dfs(s[len(piece):], dict, subset, res)
            subset.pop()