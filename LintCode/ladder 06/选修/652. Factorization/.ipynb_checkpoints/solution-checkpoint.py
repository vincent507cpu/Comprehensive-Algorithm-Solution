# https://blog.csdn.net/qq_36754149/article/details/90515301

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        if n < 3:
            return []
            
        res = []
        self.dfs(n, 2, [], res)
        return res
        
    def dfs(self, n, start, factors, res):
        if n == 1:
            if len(factors) > 1:
                res.append(list(factors))
            return
        
        for i in range(start, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                self.dfs(n // i, i, factors, res)
                factors.pop()
                
        factors.append(n)
        self.dfs(1, n, factors, res)
        factors.pop()