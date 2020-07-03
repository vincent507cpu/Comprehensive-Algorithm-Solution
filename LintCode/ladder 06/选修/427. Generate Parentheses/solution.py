class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        res = []
        self.dfs(n, n, res, '')
        return res
        
    def dfs(self, left, right, res, path):
        if left == 0 and right == 0:
            res.append(path)
            return
            
        if left > 0:
            self.dfs(left - 1, right, res, path + '(')
            
        if right > 0 and left < right:
            self.dfs(left, right - 1, res, path + ')')